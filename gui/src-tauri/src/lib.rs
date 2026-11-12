use std::path::PathBuf;
use std::process::Command;
use std::sync::OnceLock;

static PYTHON_CACHE: OnceLock<String> = OnceLock::new();
static CODE_DIR_CACHE: OnceLock<PathBuf> = OnceLock::new();

/// Locate the `code` directory containing the standalone python scripts (cached).
fn find_code_dir() -> &'static PathBuf {
    CODE_DIR_CACHE.get_or_init(|| {
        let candidates = [
            PathBuf::from("code"),
            PathBuf::from("../code"),
            PathBuf::from("../../code"),
        ];

        for c in &candidates {
            if c.is_dir() {
                return c.clone();
            }
        }

        // Fallback: search relative to executable location
        if let Ok(mut exe) = std::env::current_exe() {
            for _ in 0..5 {
                exe.pop();
                let c = exe.join("code");
                if c.is_dir() {
                    return c;
                }
            }
        }

        PathBuf::from("code")
    })
}

/// Detect and cache available Python command on the host machine.
fn find_python() -> &'static str {
    PYTHON_CACHE.get_or_init(|| {
        // 1. Direct check on common Windows install paths (bypasses slow MS Store shim)
        #[cfg(target_os = "windows")]
        {
            let fast_candidates = [
                "C:\\Python311\\python.exe",
                "C:\\Python312\\python.exe",
                "C:\\Python310\\python.exe",
                "C:\\Program Files\\Python311\\python.exe",
                "C:\\Program Files\\Python312\\python.exe",
                "C:\\Program Files\\Python310\\python.exe",
            ];
            for p in &fast_candidates {
                if std::path::Path::new(p).is_file() {
                    return p.to_string();
                }
            }
        }

        // 2. Query PATH
        for py in &["python", "py", "python3"] {
            if let Ok(out) = Command::new(py).arg("--version").output() {
                if out.status.success() {
                    return py.to_string();
                }
            }
        }

        "python".to_string()
    })
}

#[tauri::command]
#[allow(non_snake_case)]
fn run_crypto_calc(
    script_name: Option<String>,
    scriptName: Option<String>,
    args: Option<Vec<String>>,
) -> Result<String, String> {
    let script = script_name
        .or(scriptName)
        .ok_or_else(|| "Missing script name parameter".to_string())?;

    let args_list = args.unwrap_or_default();
    let code_dir = find_code_dir();
    let script_path = code_dir.join(&script);

    if !script_path.is_file() {
        return Err(format!(
            "Script file not found: {} (searched in {})",
            script,
            code_dir.display()
        ));
    }

    let python = find_python();
    let mut cmd = Command::new(python);
    // Fast flags: -B (no pyc bytecode write) and -u (unbuffered)
    cmd.arg("-B");
    cmd.arg("-u");
    // When current_dir is code_dir, script should be referenced by filename
    cmd.arg(&script);

    // Pass valid CLI arguments, filtering out empty or whitespace-only arguments
    for arg in &args_list {
        let trimmed = arg.trim();
        if !trimmed.is_empty() {
            cmd.arg(trimmed);
        }
    }

    cmd.current_dir(code_dir);

    // Completely isolate stdin to prevent Python from inheriting parent console stdin
    cmd.stdin(std::process::Stdio::null());
    cmd.env("GUI_MODE", "1");
    cmd.env("PYTHONUNBUFFERED", "1");

    // On Windows, prevent console popup if subprocess is spawned
    #[cfg(target_os = "windows")]
    {
        use std::os::windows::process::CommandExt;
        const CREATE_NO_WINDOW: u32 = 0x08000000;
        cmd.creation_flags(CREATE_NO_WINDOW);
    }

    let output = cmd
        .output()
        .map_err(|e| format!("Failed to execute '{}': {}", python, e))?;

    let stdout = String::from_utf8_lossy(&output.stdout).to_string();
    let stderr = String::from_utf8_lossy(&output.stderr).to_string();

    if !output.status.success() {
        let code = output.status.code().unwrap_or(-1);
        return Err(format!(
            "Process exited with code {}:\n{}\n{}",
            code, stdout, stderr
        ));
    }

    Ok(stdout)
}

#[tauri::command]
fn run_all_tests() -> Result<String, String> {
    run_crypto_calc(
        Some("run_all_crypto_algorithms.py".to_string()),
        None,
        Some(vec!["--demo".to_string()]),
    )
}

#[tauri::command]
fn get_student_info() -> serde_json::Value {
    serde_json::json!({
        "student_id": "23BA14056",
        "exam_number": 56,
        "course": "Introduction to Cryptography",
        "institution": "USTH - University of Science and Technology of Hanoi"
    })
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .invoke_handler(tauri::generate_handler![
            run_crypto_calc,
            run_all_tests,
            get_student_info
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_run_dhke() {
        let res = run_crypto_calc(
            Some("diffie_hellman_key_exchange.py".to_string()),
            None,
            Some(vec![
                "27361".to_string(),
                "6".to_string(),
                "20260".to_string(),
                "24372".to_string(),
            ]),
        );
        println!("RESULT: {:?}", res);
        assert!(res.is_ok());
        let out = res.unwrap();
        assert!(out.contains("k_AB = 1682"));
    }
}
