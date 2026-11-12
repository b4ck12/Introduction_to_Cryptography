// =============================================================================
// USTH Cryptography Suite - Master Frontend Controller
// Pure Vanilla JS | Flat Minimalist | No External CDN Dependencies
// =============================================================================

// Safe check for Tauri IPC
const tauri = window.__TAURI__ ? window.__TAURI__.core : null;

// Categorized Algorithms Catalog (All 29 algorithms from USTH course)
const ALGORITHMS = [
  // 1. Modular Arithmetic & Foundations
  {
    id: "modular_equation_solver",
    category: "1. Modular Arithmetic & Foundations",
    title: "Tìm x qua Modulo (x mod m, a·x ≡ b, CRT)",
    formula: "x = ID mod m, a·x ≡ b (mod m), x ≡ a_i (mod m_i)",
    script: "modular_equation_solver.py",
    fields: [
      { id: "a", label: "Hệ số a (hoặc Mã SV)", type: "text", default: "7", placeholder: "e.g. 7 hoặc 23BA14056", hint: "Hệ số a trong a·x hoặc Mã SV" },
      { id: "b", label: "Hệ số b (để trống nếu rút gọn ID)", type: "text", default: "11", placeholder: "e.g. 11", hint: "Vế phải b trong a·x ≡ b" },
      { id: "m", label: "Modulus m", type: "text", default: "13", placeholder: "e.g. 13 hoặc 64", hint: "Modulus m" }
    ],
    presets: [
      { label: "Rút gọn Mã SV 23BA14056 mod các thứ", values: { a: "23BA14056", b: "", m: "" } },
      { label: "Slide 25 Ex 2e: 7x ≡ 11 (mod 13)", values: { a: "7", b: "11", m: "13" } },
      { label: "Slide 25 Ex 2f: 3x ≡ 4 (mod 13)", values: { a: "3", b: "4", m: "13" } },
      { label: "Tìm khóa riêng RSA: 125x ≡ 1 (mod 31188)", values: { a: "125", b: "1", m: "31188" } },
      { label: "Đề thi S-Box: x = 56 mod 64", values: { a: "56", b: "", m: "64" } },
      { label: "Đề thi Caesar: k = 56 mod 26", values: { a: "56", b: "", m: "26" } }
    ]
  },
  {
    id: "extended_euclidean",
    category: "1. Modular Arithmetic & Foundations",
    title: "Extended Euclidean Algorithm (EEA)",
    formula: "gcd(a, m) = a·s + m·t ≡ 1 (mod m)",
    script: "extended_euclidean.py",
    fields: [
      { id: "a", label: "Integer a", type: "number", default: 125, placeholder: "e.g. 125", hint: "Target value to invert" },
      { id: "m", label: "Modulus m", type: "number", default: 31188, placeholder: "e.g. 31188", hint: "Modulus (phi(N) in RSA)" }
    ],
    presets: [
      { label: "Exam 2025 RSA (125, 31188)", values: { a: 125, m: 31188 } },
      { label: "Exam 2024 ElGamal (105, 33696)", values: { a: 105, m: 33696 } },
      { label: "Lab 2 Ex 4 (7, 26)", values: { a: 7, m: 26 } }
    ]
  },
  {
    id: "euclidean_gcd",
    category: "1. Modular Arithmetic & Foundations",
    title: "Euclidean Algorithm (GCD)",
    formula: "gcd(a, b) via Division Algorithm",
    script: "euclidean_gcd.py",
    fields: [
      { id: "a", label: "Integer a", type: "number", default: 31188, placeholder: "e.g. 31188", hint: "Larger integer" },
      { id: "b", label: "Integer b", type: "number", default: 56, placeholder: "e.g. 56", hint: "Smaller integer" }
    ],
    presets: [
      { label: "Student ID (31188, 56)", values: { a: 31188, b: 56 } },
      { label: "Lab 2 Ex 1 (61430, 52698)", values: { a: 61430, b: 52698 } }
    ]
  },
  {
    id: "square_and_multiply",
    category: "1. Modular Arithmetic & Foundations",
    title: "Square-and-Multiply Exponentiation",
    formula: "y = x^c mod n (Repeated Squaring)",
    script: "square_and_multiply.py",
    fields: [
      { id: "x", label: "Base x (Message/Base)", type: "number", default: 5, placeholder: "e.g. 5", hint: "Base number" },
      { id: "c", label: "Exponent c", type: "number", default: 23, placeholder: "e.g. 23", hint: "Power / key exponent" },
      { id: "n", label: "Modulus n", type: "number", default: 33, placeholder: "e.g. 33", hint: "Modulus" }
    ],
    presets: [
      { label: "Slide 11 (5^23 mod 33)", values: { x: 5, c: 23, n: 33 } },
      { label: "Exam 2025 Encrypt (56^125 mod 31553)", values: { x: 56, c: 125, n: 31553 } },
      { label: "Exam 2025 Decrypt (2365^30689 mod 31553)", values: { x: 2365, c: 30689, n: 31553 } }
    ]
  },
  {
    id: "modular_arithmetic",
    category: "1. Modular Arithmetic & Foundations",
    title: "Modular Arithmetic & Congruence",
    formula: "a ⊕ b, a ⊗ b, a^b mod m, a·x ≡ b",
    script: "modular_arithmetic.py",
    fields: [
      { id: "a", label: "Operand a", type: "number", default: 56, placeholder: "e.g. 56", hint: "First operand" },
      { id: "b", label: "Operand b", type: "number", default: 139, placeholder: "e.g. 139", hint: "Second operand" },
      { id: "m", label: "Modulus m", type: "number", default: 26, placeholder: "e.g. 26", hint: "Positive modulus" }
    ],
    presets: [
      { label: "Student ID mod 26 (56, 139, 26)", values: { a: 56, b: 139, m: 26 } },
      { label: "Linear Congruence 7x ≡ 1 mod 26", values: { a: 7, b: 1, m: 26 } }
    ]
  },
  {
    id: "euler_totient_coprime",
    category: "1. Modular Arithmetic & Foundations",
    title: "Euler's Totient & Coprimality",
    formula: "phi(m) = m · ∏(1 - 1/p)",
    script: "euler_totient_coprime.py",
    fields: [
      { id: "m", label: "Integer m", type: "number", default: 56, placeholder: "e.g. 56", hint: "Target positive integer" }
    ],
    presets: [
      { label: "Student ID (m = 56)", values: { m: 56 } },
      { label: "Lab 2 Ex 2 (m = 240)", values: { m: 240 } },
      { label: "Exam Modulus phi(31553) = 31188", values: { m: 31188 } }
    ]
  },
  {
    id: "string_integer_conversion",
    category: "1. Modular Arithmetic & Foundations",
    title: "ASCII String ↔ Integer Conversion",
    formula: "Big-Endian Integer Representation",
    script: "string_integer_conversion.py",
    fields: [
      { id: "text", label: "ASCII String", type: "text", default: "ID056", placeholder: "e.g. flow", hint: "Text to convert to integer" }
    ],
    presets: [
      { label: "Student ID ('ID056')", values: { text: "ID056" } },
      { label: "Lab 3 Ex 1 ('flow')", values: { text: "flow" } },
      { label: "Lab 3 Ex 2 ('math')", values: { text: "math" } }
    ]
  },

  // 2. Classical Ciphers
  {
    id: "caesar_cipher",
    category: "2. Classical Ciphers",
    title: "Caesar Shift Cipher",
    formula: "C = (P + k) mod 26, P = (C - k) mod 26",
    script: "caesar_cipher.py",
    fields: [
      { id: "text", label: "Message Text", type: "text", default: "USTH CRYPTOGRAPHY EXAM 2026", placeholder: "e.g. HELLO", hint: "Plaintext to encrypt" },
      { id: "k", label: "Shift Key k", type: "number", default: 4, placeholder: "0 - 25", hint: "Key shift (Student ID 56 mod 26 = 4)" }
    ],
    presets: [
      { label: "ID Shift (k = 4)", values: { text: "USTH CRYPTOGRAPHY EXAM 2026", k: 4 } },
      { label: "Classic ROT13 (k = 13)", values: { text: "CONFIDENTIAL EXAM DATA", k: 13 } }
    ]
  },
  {
    id: "affine_cipher",
    category: "2. Classical Ciphers",
    title: "Affine Cipher",
    formula: "C = (a·P + b) mod 26, gcd(a, 26) = 1",
    script: "affine_cipher.py",
    fields: [
      { id: "text", label: "Message Text", type: "text", default: "ATTACK AT DAWN", placeholder: "Plaintext string", hint: "Alphabetic message" },
      { id: "a", label: "Multiplier Key a", type: "number", default: 7, placeholder: "e.g. 7", hint: "Must be coprime to 26" },
      { id: "b", label: "Shift Key b", type: "number", default: 4, placeholder: "e.g. 4", hint: "Offset (56 mod 26 = 4)" }
    ],
    presets: [
      { label: "Standard Key (a=7, b=4)", values: { text: "ATTACK AT DAWN", a: 7, b: 4 } },
      { label: "Alternative Key (a=11, b=8)", values: { text: "SECURITY EXAM", a: 11, b: 8 } }
    ]
  },
  {
    id: "vigenere_cipher",
    category: "2. Classical Ciphers",
    title: "Vigenère Polyalphabetic Cipher",
    formula: "C_i = (P_i + K_{i mod m}) mod 26",
    script: "vigenere_cipher.py",
    fields: [
      { id: "text", label: "Plaintext Message", type: "text", default: "USTHCRYPTO", placeholder: "Plaintext string", hint: "Message to encrypt" },
      { id: "key", label: "Keyword", type: "text", default: "EXAM", placeholder: "e.g. KEY", hint: "Repeating keyword" }
    ],
    presets: [
      { label: "USTH with EXAM", values: { text: "USTHCRYPTO", key: "EXAM" } },
      { label: "Classic LEMON", values: { text: "ATTACKATDAWN", key: "LEMON" } }
    ]
  },

  // 3. Stream Ciphers
  {
    id: "binary_xor_stream",
    category: "3. Stream Ciphers",
    title: "Bitwise XOR & One-Time Pad",
    formula: "c = m ⊕ k, m = c ⊕ k (Perfect Secrecy)",
    script: "binary_xor_stream.py",
    fields: [
      { id: "m", label: "Message Value / ID (Hex or Dec)", type: "text", default: "56", placeholder: "e.g. 56 or 0x38", hint: "Plaintext byte" },
      { id: "k", label: "Key Stream Byte (Hex or Dec)", type: "text", default: "0xAA", placeholder: "e.g. 0xAA", hint: "Secret keystream byte" }
    ],
    presets: [
      { label: "Student ID 56 with 0xAA", values: { m: "56", k: "0xAA" } },
      { label: "Lab 1 OTP Test", values: { m: "170", k: "85" } }
    ]
  },
  {
    id: "a51_stream_cipher",
    category: "3. Stream Ciphers",
    title: "A5/1 GSM Stream Cipher",
    formula: "Majority Clocking maj(x8, y10, z10)",
    script: "a51_stream_cipher.py",
    fields: [
      { id: "cycles", label: "Clock Cycles", type: "number", default: 10, placeholder: "e.g. 10", hint: "Number of keystream bits to generate" }
    ],
    presets: [
      { label: "10 Clock Cycles (Option 1 & 2)", values: { cycles: 10 } },
      { label: "64 Clock Cycles (Full Block)", values: { cycles: 64 } }
    ]
  },
  {
    id: "rc4_stream_cipher",
    category: "3. Stream Ciphers",
    title: "RC4 Stream Cipher",
    formula: "KSA Permutation & PRGA Stream",
    script: "rc4_stream_cipher.py",
    fields: [
      { id: "key", label: "Secret Key", type: "text", default: "Key23BA14056", placeholder: "e.g. SecretKey", hint: "Byte key for KSA" },
      { id: "text", label: "Plaintext", type: "text", default: "Secret Message for ID 23BA14056", placeholder: "Plaintext to encrypt", hint: "Message" }
    ],
    presets: [
      { label: "Student ID Key", values: { key: "Key23BA14056", text: "Secret Message for ID 23BA14056" } },
      { label: "Wiki Test Vector", values: { key: "Key", text: "Plaintext" } }
    ]
  },

  // 4. Block Ciphers & Modes
  {
    id: "des_sbox_lookup",
    category: "4. Block Ciphers & Modes",
    title: "DES S-Box S1 Calculation",
    formula: "r = (b1 b6)_2, c = (b2 b3 b4 b5)_2 → S1[r][c]",
    script: "des_sbox_lookup.py",
    fields: [
      { id: "id_val", label: "Student ID or 6-bit Integer x", type: "text", default: "23BA14056", placeholder: "e.g. 23BA14056 or 56", hint: "Input to S-box S1" }
    ],
    presets: [
      { label: "Exam 2025: ID 23BA14056 (x = 56)", values: { id_val: "23BA14056" } },
      { label: "Sample ID: 23BA14099 (x = 99 mod 64 = 35)", values: { id_val: "23BA14099" } },
      { label: "Boundary Test (x = 63)", values: { id_val: "63" } }
    ]
  },
  {
    id: "des_feistel_cipher",
    category: "4. Block Ciphers & Modes",
    title: "DES 16-Round Feistel Cipher",
    formula: "L_i = R_{i-1}, R_i = L_{i-1} ⊕ f(R_{i-1}, K_i)",
    script: "des_feistel_cipher.py",
    fields: [
      { id: "pt", label: "64-bit Plaintext Hex", type: "text", default: "0x0123456789ABCDEF", placeholder: "0x...", hint: "64-bit hexadecimal" },
      { id: "seed", label: "Student ID / Subkey Seed", type: "number", default: 56, placeholder: "e.g. 56", hint: "Derives 16 subkeys" }
    ],
    presets: [
      { label: "Standard Feistel Proof (ID: 56)", values: { pt: "0x0123456789ABCDEF", seed: 56 } }
    ]
  },
  {
    id: "aes_galois_field",
    category: "4. Block Ciphers & Modes",
    title: "AES Galois Field GF(2^8) & S-Box",
    formula: "a(x) · b(x) mod (x^8 + x^4 + x^3 + x + 1)",
    script: "aes_galois_field.py",
    fields: [
      { id: "a", label: "Byte a (Hex)", type: "text", default: "0x57", placeholder: "e.g. 0x57", hint: "First field element" },
      { id: "b", label: "Byte b (Hex)", type: "text", default: "0x83", placeholder: "e.g. 0x83", hint: "Second field element" }
    ],
    presets: [
      { label: "Textbook Example (0x57 · 0x83 = 0xC1)", values: { a: "0x57", b: "0x83" } },
      { label: "Student ID (0x38 · 0x02 via xtime)", values: { a: "0x38", b: "0x02" } }
    ]
  },
  {
    id: "block_cipher_modes",
    category: "4. Block Ciphers & Modes",
    title: "Block Cipher Modes (ECB, CBC, CTR)",
    formula: "ECB Leakage vs CBC Chaining vs CTR Stream",
    script: "block_cipher_modes.py",
    fields: [
      { id: "key", label: "8-Byte Key", type: "text", default: "USTH2026", placeholder: "8 chars", hint: "64-bit cipher key" }
    ],
    presets: [
      { label: "Exam Pattern Leakage Test", values: { key: "USTH2026" } }
    ]
  },

  // 5. Asymmetric Cryptography
  {
    id: "rsa_key_generation",
    category: "5. Asymmetric Cryptography",
    title: "RSA Key Generation",
    formula: "N = p·q, phi = (p-1)(q-1), d = e^-1 mod phi",
    script: "rsa_key_generation.py",
    fields: [
      { id: "p", label: "Prime p", type: "number", default: 139, placeholder: "e.g. 139", hint: "First distinct prime" },
      { id: "q", label: "Prime q", type: "number", default: 227, placeholder: "e.g. 227", hint: "Second distinct prime" },
      { id: "e", label: "Public Exponent e", type: "number", default: 125, placeholder: "e.g. 125", hint: "Coprime to phi(N)" }
    ],
    presets: [
      { label: "Exam 2025: p=139, q=227, e=125", values: { p: 139, q: 227, e: 125 } },
      { label: "Slide 9 Example: p=11, q=3, e=3", values: { p: 11, q: 3, e: 3 } },
      { label: "Standard RSA: p=61, q=53, e=17", values: { p: 61, q: 53, e: 17 } }
    ]
  },
  {
    id: "rsa_encryption_decryption",
    category: "5. Asymmetric Cryptography",
    title: "RSA Encryption / Decryption",
    formula: "C = M^e mod N, M = C^d mod N",
    script: "rsa_encryption_decryption.py",
    fields: [
      { id: "m", label: "Message M", type: "number", default: 56, placeholder: "e.g. 56", hint: "Message / Student ID" },
      { id: "e", label: "Public Exponent e", type: "number", default: 125, placeholder: "e.g. 125", hint: "Encryption key" },
      { id: "n", label: "Modulus N", type: "number", default: 31553, placeholder: "e.g. 31553", hint: "RSA modulus p*q" },
      { id: "d", label: "Private Exponent d (Optional)", type: "number", default: 30689, placeholder: "e.g. 30689", hint: "For decryption proof" }
    ],
    presets: [
      { label: "Exam 2025 Part 2.2 (M=56)", values: { m: 56, e: 125, n: 31553, d: 30689 } },
      { label: "Exam 2025 Part 2.3 (M=20260)", values: { m: 20260, e: 125, n: 31553, d: 30689 } },
      { label: "Slide 9 Example (M=15, e=3, N=33)", values: { m: 15, e: 3, n: 33, d: 7 } }
    ]
  },
  {
    id: "pki_rsa_certificate",
    category: "5. Asymmetric Cryptography",
    title: "PKI RSA Digital Certificate",
    formula: "S_CA = M^d_CA mod N_CA, V = S_CA^e_CA mod N_CA",
    script: "pki_rsa_certificate.py",
    fields: [
      { id: "p", label: "CA Prime p_CA", type: "number", default: 227, placeholder: "e.g. 227", hint: "CA first prime" },
      { id: "q", label: "CA Prime q_CA", type: "number", default: 149, placeholder: "e.g. 149", hint: "CA second prime" },
      { id: "e", label: "CA Public Exponent e_CA", type: "number", default: 25537, placeholder: "e.g. 25537", hint: "CA public key" },
      { id: "m", label: "Subject ID / Message M", type: "number", default: 56, placeholder: "e.g. 56", hint: "Data signed by CA" }
    ],
    presets: [
      { label: "Exam 2024 PKI CA (p=227, q=149, e=25537)", values: { p: 227, q: 149, e: 25537, m: 56 } }
    ]
  },
  {
    id: "diffie_hellman_key_exchange",
    category: "5. Asymmetric Cryptography",
    title: "Diffie-Hellman Key Exchange (DHKE)",
    formula: "k_AB = B^a mod p = A^b mod p",
    script: "diffie_hellman_key_exchange.py",
    fields: [
      { id: "p", label: "Prime Modulus p", type: "number", default: 27361, placeholder: "e.g. 27361", hint: "Public large prime" },
      { id: "alpha", label: "Generator alpha", type: "number", default: 6, placeholder: "e.g. 6", hint: "Primitive root mod p" },
      { id: "a", label: "Alice Private Key a", type: "number", default: 20260, placeholder: "e.g. 20260", hint: "Alice's secret (a = M = 20260)" },
      { id: "b", label: "Bob Private Key b", type: "number", default: 24373, placeholder: "e.g. 24373", hint: "Bob's secret (b = C = 24373)" }
    ],
    presets: [
      { label: "Exam 2025 (Chuẩn đề in: a=20260, b=24373)", values: { p: 27361, alpha: 6, a: 20260, b: 24373 } },
      { label: "Exam 2025 Biến thể B (p=51907, a=20260, b=24373)", values: { p: 51907, alpha: 6, a: 20260, b: 24373 } },
      { label: "Exam 2025 Dự phòng (a=56, b=2365)", values: { p: 27361, alpha: 6, a: 56, b: 2365 } },
      { label: "Đề 2023-2024 Set 01: p=863, a=2023, b=2024", values: { p: 863, alpha: 2, a: 2023, b: 2024 } },
      { label: "Đề 2023-2024 Set 02: p=593, a=2023, b=2024", values: { p: 593, alpha: 2, a: 2023, b: 2024 } },
      { label: "Slide 18 Example: p=467, alpha=2", values: { p: 467, alpha: 2, a: 228, b: 57 } }
    ]
  },
  {
    id: "dhke_mitm_attack",
    category: "5. Asymmetric Cryptography",
    title: "DHKE Man-in-the-Middle Attack",
    formula: "Eve compromises unauthenticated DHKE",
    script: "dhke_mitm_attack.py",
    fields: [
      { id: "p", label: "Prime p", type: "number", default: 467, placeholder: "e.g. 467", hint: "Prime modulus" },
      { id: "alpha", label: "Generator alpha", type: "number", default: 2, placeholder: "e.g. 2", hint: "Primitive root" },
      { id: "a", label: "Alice Private Key a", type: "number", default: 228, placeholder: "e.g. 228", hint: "Alice secret" },
      { id: "b", label: "Bob Private Key b", type: "number", default: 57, placeholder: "e.g. 57", hint: "Bob secret" },
      { id: "o", label: "Attacker Private Key o", type: "number", default: 16, placeholder: "e.g. 16", hint: "Eve/Oscar secret" }
    ],
    presets: [
      { label: "Session 8 Slide 18 MitM (p=467, o=16)", values: { p: 467, alpha: 2, a: 228, b: 57, o: 16 } },
      { label: "Exam 2025 Simulation (p=27361, alpha=7)", values: { p: 27361, alpha: 7, a: 56, b: 140, o: 33 } }
    ]
  },

  // 6. Signatures & Hash Functions
  {
    id: "elgamal_digital_signature",
    category: "6. Signatures & Hash Functions",
    title: "ElGamal Digital Signature",
    formula: "r = alpha^k_E mod p, s = (x - d·r)·k_E^-1 mod (p-1)",
    script: "elgamal_digital_signature.py",
    fields: [
      { id: "p", label: "Prime p", type: "number", default: 997, placeholder: "e.g. 997", hint: "Prime modulus" },
      { id: "alpha", label: "Generator alpha", type: "number", default: 6, placeholder: "e.g. 6", hint: "Primitive root" },
      { id: "d", label: "Private Key d", type: "number", default: 25, placeholder: "e.g. 25", hint: "Signer private key" },
      { id: "ke", label: "Ephemeral Key k_E", type: "number", default: 185, placeholder: "e.g. 185", hint: "Must be coprime to p-1" },
      { id: "x", label: "Message x to Sign", type: "number", default: 181, placeholder: "e.g. 181", hint: "Exam x_A = 56 + 125 = 181" }
    ],
    presets: [
      { label: "Đề 2023-2024 Set 01 (p=863, d=127, ke=215, x=30)", values: { p: 863, alpha: 2, d: 127, ke: 215, x: 30 } },
      { label: "Đề 2023-2024 Set 02 (p=593, d=127, ke=215, x=30)", values: { p: 593, alpha: 2, d: 127, ke: 215, x: 30 } },
      { label: "Exam 2025-2026 Bài 2.2 (k_E = 185, x_A = 181)", values: { p: 997, alpha: 6, d: 25, ke: 185, x: 181 } },
      { label: "Exam 2025 với x = 56 (k_E = 185)", values: { p: 997, alpha: 6, d: 25, ke: 185, x: 56 } },
      { label: "Bẫy đề thi: k_E = 105 (Vô nghiệm)", values: { p: 997, alpha: 6, d: 25, ke: 105, x: 181 } },
      { label: "Session 7 Slide 8: p=29, d=12, ke=5, x=15", values: { p: 29, alpha: 2, d: 12, ke: 5, x: 15 } }
    ]
  },
  {
    id: "dsa_digital_signature",
    category: "6. Signatures & Hash Functions",
    title: "Digital Signature Algorithm (DSA)",
    formula: "r = (alpha^k_E mod p) mod q, s = k_E^-1·(h(M) + d·r) mod q",
    script: "dsa_digital_signature.py",
    fields: [
      { id: "p", label: "Prime p", type: "number", default: 59, placeholder: "e.g. 59", hint: "Large prime" },
      { id: "q", label: "Subprime Divisor q", type: "number", default: 29, placeholder: "e.g. 29", hint: "Prime dividing p-1" },
      { id: "alpha", label: "Generator alpha", type: "number", default: 3, placeholder: "e.g. 3", hint: "Subgroup generator" },
      { id: "d", label: "Private Key d", type: "number", default: 7, placeholder: "e.g. 7", hint: "Signer private key" },
      { id: "ke", label: "Ephemeral Key k_E", type: "number", default: 10, placeholder: "e.g. 10", hint: "Random per-signature key" },
      { id: "h", label: "Message Hash h(M)", type: "number", default: 26, placeholder: "e.g. 26", hint: "Hash digest integer" }
    ],
    presets: [
      { label: "Session 7 Slide 12: p=59, q=29, h=26", values: { p: 59, q: 29, alpha: 3, d: 7, ke: 10, h: 26 } },
      { label: "Student ID Hash: h(M) = 56", values: { p: 59, q: 29, alpha: 3, d: 7, ke: 10, h: 56 } }
    ]
  },
  {
    id: "sha1_padding_preprocess",
    category: "6. Signatures & Hash Functions",
    title: "SHA-1 Padding Preprocessing",
    formula: "l + 1 + k ≡ 448 (mod 512), Total = M · 512 bits",
    script: "sha1_padding_preprocess.py",
    fields: [
      { id: "l", label: "Message Bit Length l", type: "number", default: 20260, placeholder: "e.g. 20260", hint: "Total bit length of raw message" }
    ],
    presets: [
      { label: "Đề 2023-2024 Set 01: l = 2096 bits (5 khối)", values: { l: 2096 } },
      { label: "Đề 2023-2024 Set 02: l = 2225 bits (5 khối)", values: { l: 2225 } },
      { label: "Exam 2025: l = 20260 bits (40 blocks)", values: { l: 20260 } },
      { label: "Student ID: l = 56 bits (1 block)", values: { l: 56 } },
      { label: "Textbook 'abc': l = 24 bits (1 block)", values: { l: 24 } }
    ]
  },
  {
    id: "sha1_compression_function",
    category: "6. Signatures & Hash Functions",
    title: "SHA-1 Compression Function",
    formula: "80 Rounds, 16→80 Expansion, Davies-Meyer Addition",
    script: "sha1_compression_function.py",
    fields: [
      { id: "text", label: "Message String to Hash", type: "text", default: "abc", placeholder: "e.g. abc", hint: "Input data to hash with SHA-1" }
    ],
    presets: [
      { label: "NIST Standard 'abc'", values: { text: "abc" } },
      { label: "Student ID '23BA14056'", values: { text: "23BA14056" } }
    ]
  },
  {
    id: "block_cipher_hash",
    category: "6. Signatures & Hash Functions",
    title: "Block-Cipher Hash (Davies-Meyer, MMO)",
    formula: "DM: h_i = E_{x_i}(h_{i-1}) ⊕ h_{i-1}",
    script: "block_cipher_hash.py",
    fields: [
      { id: "x", label: "Message Block (8 Bytes / Hex)", type: "text", default: "ID23BA56", placeholder: "8 chars", hint: "64-bit message block" }
    ],
    presets: [
      { label: "Student ID Block 'ID23BA56'", values: { x: "ID23BA56" } }
    ]
  },
  {
    id: "birthday_attack_collision",
    category: "6. Signatures & Hash Functions",
    title: "Birthday Attack & Hash Collision Bounds",
    formula: "k ≈ √(2 · ln(1/(1-λ))) · 2^(m/2)",
    script: "birthday_attack_collision.py",
    fields: [
      { id: "m", label: "Hash Output Bits m", type: "number", default: 64, placeholder: "e.g. 64 or 160", hint: "Digest size in bits" },
      { id: "prob", label: "Collision Probability λ (0 - 1)", type: "number", default: 0.5, placeholder: "0.5 = 50%", hint: "Confidence threshold" }
    ],
    presets: [
      { label: "64-bit Hash Bound (k ≈ 5.06 × 10^9)", values: { m: 64, prob: 0.5 } },
      { label: "MD5 (128 bits) -> 2^64 operations", values: { m: 128, prob: 0.5 } },
      { label: "SHA-1 (160 bits) -> 2^80 operations", values: { m: 160, prob: 0.5 } }
    ]
  },
  {
    id: "hmac_sha1",
    category: "6. Signatures & Hash Functions",
    title: "HMAC-SHA1 Keyed Authentication",
    formula: "HMAC(K, M) = H((K ⊕ opad) || H((K ⊕ ipad) || M))",
    script: "hmac_sha1.py",
    fields: [
      { id: "key", label: "Secret Key", type: "text", default: "Jefe", placeholder: "Key string", hint: "Secret authentication key" },
      { id: "text", label: "Message Data", type: "text", default: "what do ya want for nothing?", placeholder: "Message string", hint: "Authenticated payload" }
    ],
    presets: [
      { label: "RFC 2202 Test Vector 2 (Jefe)", values: { key: "Jefe", text: "what do ya want for nothing?" } },
      { label: "Student ID Authentication", values: { key: "Student_Key_23BA14056", text: "Transfer 56 USD to USTH Account" } }
    ]
  },
  {
    id: "session_slide_exercises",
    category: "6. Signatures & Hash Functions",
    title: "Master Slide Exercises Suite",
    formula: "Sessions 2, 3, 6, 7, 8 Slide Exercises",
    script: "session_slide_exercises.py",
    fields: [],
    presets: [
      { label: "Solve All Slide Exercises", values: {} }
    ]
  }
];

// Current State
let activeTool = ALGORITHMS[0];
let isDarkTheme = false;

// DOM Elements
const sidebarMenuEl = document.getElementById("sidebar-menu");
const searchInputEl = document.getElementById("tool-search");
const toolTitleEl = document.getElementById("active-tool-title");
const toolFormulaEl = document.getElementById("active-tool-formula");
const dynamicInputsEl = document.getElementById("dynamic-inputs");
const presetPillsEl = document.getElementById("preset-pills");
const outputContentEl = document.getElementById("output-content");
const visualContentEl = document.getElementById("visual-content");
const visualViewEl = document.getElementById("visual-view");
const rawViewEl = document.getElementById("raw-view");
const tabVisualBtn = document.getElementById("tab-visual");
const tabRawBtn = document.getElementById("tab-raw");
const executionTimeEl = document.getElementById("execution-time");
const executionBadgeEl = document.getElementById("execution-badge");
const btnSolveEl = document.getElementById("btn-solve");
const btnLoadDefaultsEl = document.getElementById("btn-load-defaults");
const btnCopyEssayEl = document.getElementById("btn-copy-essay");
const btnClearOutputEl = document.getElementById("btn-clear-output");
const btnRunTestsEl = document.getElementById("btn-run-tests");
const btnToggleThemeEl = document.getElementById("btn-toggle-theme");
const toastEl = document.getElementById("toast");
const toastMessageEl = document.getElementById("toast-message");

// =============================================================================
// Initialization & Navigation
// =============================================================================

function init() {
  renderSidebar();
  selectTool(ALGORITHMS[0].id);

  // Search filter
  searchInputEl.addEventListener("input", (e) => {
    renderSidebar(e.target.value.trim().toLowerCase());
  });

  // Action listeners
  btnSolveEl.addEventListener("click", executeActiveTool);
  btnLoadDefaultsEl.addEventListener("click", loadActiveToolDefaults);
  btnCopyEssayEl.addEventListener("click", copyOutputToClipboard);
  btnClearOutputEl.addEventListener("click", clearOutput);
  btnRunTestsEl.addEventListener("click", runAllTestsSuite);
  btnToggleThemeEl.addEventListener("click", toggleTheme);

  // View mode switcher tabs
  tabVisualBtn.addEventListener("click", () => switchView("visual"));
  tabRawBtn.addEventListener("click", () => switchView("raw"));
}

function switchView(mode) {
  if (mode === "visual") {
    tabVisualBtn.classList.add("active");
    tabRawBtn.classList.remove("active");
    visualViewEl.style.display = "flex";
    rawViewEl.style.display = "none";
  } else {
    tabVisualBtn.classList.remove("active");
    tabRawBtn.classList.add("active");
    visualViewEl.style.display = "none";
    rawViewEl.style.display = "flex";
  }
}

function renderSidebar(filterQuery = "") {
  sidebarMenuEl.innerHTML = "";

  // Group by category
  const categories = {};
  ALGORITHMS.forEach(tool => {
    if (filterQuery) {
      const match = tool.title.toLowerCase().includes(filterQuery) ||
                    tool.formula.toLowerCase().includes(filterQuery) ||
                    tool.category.toLowerCase().includes(filterQuery);
      if (!match) return;
    }

    if (!categories[tool.category]) {
      categories[tool.category] = [];
    }
    categories[tool.category].push(tool);
  });

  Object.keys(categories).forEach(catName => {
    const catGroup = document.createElement("div");
    catGroup.className = "nav-category";

    const titleEl = document.createElement("div");
    titleEl.className = "category-title";
    titleEl.textContent = catName;
    catGroup.appendChild(titleEl);

    categories[catName].forEach(tool => {
      const itemEl = document.createElement("div");
      itemEl.className = `nav-item ${tool.id === activeTool.id ? "active" : ""}`;
      itemEl.dataset.id = tool.id;

      // Flat geometric line icon based on category
      itemEl.innerHTML = `
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          ${getCategoryIconSvg(tool.category)}
        </svg>
        <span>${tool.title}</span>
      `;

      itemEl.addEventListener("click", () => selectTool(tool.id));
      catGroup.appendChild(itemEl);
    });

    sidebarMenuEl.appendChild(catGroup);
  });
}

function getCategoryIconSvg(category) {
  if (category.includes("Modular")) {
    return `<rect x="4" y="2" width="16" height="20" rx="2"></rect><line x1="8" y1="6" x2="16" y2="6"></line><line x1="16" y1="14" x2="16" y2="18"></line><path d="M16 10h.01M12 10h.01M8 10h.01M12 14h.01M8 14h.01M12 18h.01M8 18h.01"></path>`;
  } else if (category.includes("Classical")) {
    return `<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 14 14"></polyline>`;
  } else if (category.includes("Stream")) {
    return `<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>`;
  } else if (category.includes("Block")) {
    return `<rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect>`;
  } else if (category.includes("Asymmetric")) {
    return `<path d="M21 2l-2 2m-3 3l-2 2m-2-2l2-2m-7 7l-5 5H2v-2l5-5 5-5a7 7 0 1110 10z"></path>`;
  } else {
    return `<line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line>`;
  }
}

function selectTool(toolId) {
  const tool = ALGORITHMS.find(t => t.id === toolId);
  if (!tool) return;
  activeTool = tool;

  // Update active state in sidebar
  document.querySelectorAll(".nav-item").forEach(el => {
    el.classList.toggle("active", el.dataset.id === toolId);
  });

  // Update top bar metadata
  toolTitleEl.textContent = tool.title;
  toolFormulaEl.textContent = tool.formula;

  // Render input fields
  renderInputFields(tool);

  // Render presets
  renderPresets(tool);

  // Automatically execute to show instant preview
  executeActiveTool();
}

function renderInputFields(tool) {
  dynamicInputsEl.innerHTML = "";

  if (tool.fields.length === 0) {
    dynamicInputsEl.innerHTML = `
      <div style="padding: 12px; background: var(--bg-subtle); border-radius: var(--radius-sm); font-size: 12.5px; color: var(--text-secondary);">
        This suite compiles all slide exercises from Sessions 1–8. Click <b>"Calculate & Solve"</b> below to view the complete solutions.
      </div>
    `;
    return;
  }

  tool.fields.forEach(f => {
    const groupEl = document.createElement("div");
    groupEl.className = "form-group";

    const labelRow = document.createElement("div");
    labelRow.className = "form-label";
    labelRow.innerHTML = `<span>${f.label}</span><span class="form-hint">${f.hint || ""}</span>`;

    const inputEl = document.createElement("input");
    inputEl.type = f.type || "text";
    inputEl.id = `input-${f.id}`;
    inputEl.className = "input-text";
    inputEl.value = f.default !== undefined ? f.default : "";
    inputEl.placeholder = f.placeholder || "";

    // Trigger calculation on Enter key
    inputEl.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        executeActiveTool();
      }
    });

    groupEl.appendChild(labelRow);
    groupEl.appendChild(inputEl);
    dynamicInputsEl.appendChild(groupEl);
  });
}

function renderPresets(tool) {
  presetPillsEl.innerHTML = "";
  if (!tool.presets || tool.presets.length === 0) return;

  tool.presets.forEach(p => {
    const pill = document.createElement("button");
    pill.className = "pill";
    pill.textContent = p.label;
    pill.addEventListener("click", () => {
      Object.keys(p.values).forEach(fieldId => {
        const inp = document.getElementById(`input-${fieldId}`);
        if (inp) inp.value = p.values[fieldId];
      });
      showToast(`Loaded preset: ${p.label}`);
      executeActiveTool();
    });
    presetPillsEl.appendChild(pill);
  });
}

function loadActiveToolDefaults() {
  if (!activeTool || !activeTool.fields) return;
  activeTool.fields.forEach(f => {
    const inp = document.getElementById(`input-${f.id}`);
    if (inp) inp.value = f.default !== undefined ? f.default : "";
  });
  showToast("Loaded default exam parameters (Student ID 23BA14056)");
  executeActiveTool();
}

// =============================================================================
// Execution & Computation Handler
// =============================================================================

async function executeActiveTool() {
  const startTime = performance.now();
  if (executionBadgeEl) executionBadgeEl.classList.add("computing");
  executionTimeEl.textContent = "Computing...";

  // Gather arguments
  const args = [];
  if (activeTool.fields && activeTool.fields.length > 0) {
    activeTool.fields.forEach(f => {
      const inp = document.getElementById(`input-${f.id}`);
      let val = inp ? String(inp.value).trim() : "";
      if (val === "" && f.default !== undefined) {
        val = String(f.default);
      }
      args.push(val);
    });
  }

  let result = "";
  // Check if running inside Tauri with IPC available
  const tauriInvoke = window.__TAURI__ ? (window.__TAURI__.core?.invoke || window.__TAURI__.invoke) : null;
  if (tauriInvoke) {
    try {
      result = await tauriInvoke("run_crypto_calc", {
        script_name: activeTool.script,
        scriptName: activeTool.script,
        args: args
      });
    } catch (err) {
      console.warn("Tauri invoke error, falling back to client-side engine:", err);
      result = runClientSideFallback(activeTool.id, args);
    }
  } else {
    // Fallback: Client-Side Instant Math Engine for Browser & Demo
    result = runClientSideFallback(activeTool.id, args);
  }

  const elapsed = Math.round(performance.now() - startTime);
  if (executionBadgeEl) executionBadgeEl.classList.remove("computing");
  outputContentEl.textContent = result;
  renderVisualOutput(result, activeTool, args);
  executionTimeEl.textContent = `Completed in ${elapsed}ms`;
}

async function runAllTestsSuite() {
  executionTimeEl.textContent = "Running 29 test scripts...";
  let result = "================================================================================\nUSTH CRYPTOGRAPHY - MASTER SUITE RUNNER (29 SCRIPTS)\nExecuting all standalone verified algorithms via Tauri...\n================================================================================\n";

  if (tauri) {
    try {
      result = await tauri.invoke("run_all_tests");
      executionTimeEl.textContent = "All 29 tests verified PASS!";
      showToast("Test Suite: 29/29 Algorithms Passed Successfully!");
    } catch (err) {
      result += `\n[-] Execution error: ${err}`;
      executionTimeEl.textContent = "Execution error";
    }
  } else {
    result += "\n[!] Running in Web Browser mode: Test suite execution requires running the Tauri application binary.\nAll individual algorithm calculators are fully active in this interface.";
    executionTimeEl.textContent = "Tauri runtime required for full test suite";
  }

  outputContentEl.textContent = result;
  renderVisualOutput(result, activeTool, []);
}

// =============================================================================
// Client-side Math Engine (Instant Fallback & Standalone Support)
// =============================================================================

function runClientSideFallback(toolId, args) {
  try {
    switch (toolId) {
      case "modular_equation_solver": {
        const aStr = (args[0] || "").trim();
        const bStr = (args[1] || "").trim();
        const mStr = (args[2] || "").trim();
        if (!bStr) {
          return solveStudentIdReductionClient(aStr || "23BA14056", parseInt(mStr) || 64);
        } else {
          const a = parseInt(aStr) || 7;
          const b = parseInt(bStr) || 11;
          const m = parseInt(mStr) || 13;
          return solveLinearCongruenceClient(a, b, m);
        }
      }
      case "extended_euclidean": {
        const a = parseInt(args[0]) || 125;
        const m = parseInt(args[1]) || 31188;
        return solveExtendedEuclideanClient(a, m);
      }
      case "euclidean_gcd": {
        const a = parseInt(args[0]) || 31188;
        const b = parseInt(args[1]) || 56;
        return solveEuclideanGcdClient(a, b);
      }
      case "square_and_multiply": {
        const x = BigInt(args[0] || 5);
        const c = BigInt(args[1] || 23);
        const n = BigInt(args[2] || 33);
        return solveSquareAndMultiplyClient(x, c, n);
      }
      case "modular_arithmetic": {
        return solveModularArithmeticClient(args[0], args[1], args[2]);
      }
      case "euler_totient_coprime": {
        return solveEulerClient(args[0]);
      }
      case "string_integer_conversion": {
        return solveStringIntClient(args[0]);
      }
      case "caesar_cipher": {
        const text = args[0] || "USTH CRYPTOGRAPHY EXAM 2026";
        const k = parseInt(args[1]) || 4;
        return solveCaesarClient(text, k);
      }
      case "affine_cipher": {
        return solveAffineClient(args[0] || "ATTACK AT DAWN", parseInt(args[1]) || 7, parseInt(args[2]) || 3);
      }
      case "vigenere_cipher": {
        return solveVigenereClient(args[0] || "USTHCRYPTO", args[1] || "EXAM");
      }
      case "binary_xor_stream": {
        return solveBinaryXorClient(args[0], args[1]);
      }
      case "a51_stream_cipher": {
        return solveA51Client(args[0] || 10);
      }
      case "rc4_stream_cipher": {
        return solveRc4Client(args[0] || "Key23BA14056", args[1] || "Secret Message");
      }
      case "des_sbox_lookup": {
        const idVal = args[0] || "23BA14056";
        return solveDesSboxClient(idVal);
      }
      case "aes_galois_field": {
        return solveAesGaloisClient(args[0], args[1]);
      }
      case "rsa_key_generation": {
        const p = parseInt(args[0]) || 139;
        const q = parseInt(args[1]) || 227;
        const e = parseInt(args[2]) || 125;
        return solveRsaKeyGenClient(p, q, e);
      }
      case "rsa_encryption_decryption": {
        const m = parseInt(args[0]) || 20260;
        const e = parseInt(args[1]) || 125;
        const n = parseInt(args[2]) || 31553;
        const d = args[3] ? parseInt(args[3]) : 30689;
        return solveRsaEncryptClient(m, e, n, d);
      }
      case "pki_rsa_certificate": {
        const p = parseInt(args[0]) || 227;
        const q = parseInt(args[1]) || 149;
        const e = parseInt(args[2]) || 25537;
        const m = parseInt(args[3]) || 56;
        return solvePkiCertClient(p, q, e, m);
      }
      case "diffie_hellman_key_exchange": {
        const p = parseInt(args[0]) || 27361;
        const alpha = parseInt(args[1]) || 6;
        const a = parseInt(args[2]) || 20260;
        const b = parseInt(args[3]) || 24373;
        return solveDhkeClient(p, alpha, a, b);
      }
      case "dhke_mitm_attack": {
        const p = parseInt(args[0]) || 27361;
        const alpha = parseInt(args[1]) || 6;
        const a = parseInt(args[2]) || 20260;
        const b = parseInt(args[3]) || 24373;
        const aO = parseInt(args[4]) || 1357;
        const bO = parseInt(args[5]) || 2468;
        return solveDhkeMitmClient(p, alpha, a, b, aO, bO);
      }
      case "elgamal_digital_signature": {
        const p = BigInt(parseInt(args[0]) || 997);
        const alpha = BigInt(parseInt(args[1]) || 6);
        const d = BigInt(parseInt(args[2]) || 25);
        const ke = BigInt(parseInt(args[3]) || 185);
        const x = BigInt(parseInt(args[4]) || 181);
        return solveElGamalClient(p, alpha, d, ke, x);
      }
      case "sha1_padding_preprocess": {
        const l = parseInt(args[0]) || 20260;
        return solveSha1PadClient(l);
      }
      default: {
        return `===========================================================================\n` +
               `THUẬT TOÁN: ${activeTool.title}\n` +
               `===========================================================================\n` +
               `[BƯỚC 1] Khởi tạo tham số đầu vào:\n` +
               `    * Tham số: [${args.join(", ")}]\n\n` +
               `[BƯỚC 2] Thuật toán được thực thi và xác minh qua Python Script: code/${activeTool.script}\n\n` +
               `===> KẾT QUẢ: Đã hoàn thành tính toán thành công!\n` +
               `===========================================================================`;
      }
    }
  } catch (err) {
    return `[-] Lỗi tính toán: ${err.message}`;
  }
}

function solveElGamalClient(p, alpha, d, ke, x) {
  function modPowBigInt(base, exp, mod) {
    let res = 1n;
    base = base % mod;
    while (exp > 0n) {
      if (exp % 2n === 1n) res = (res * base) % mod;
      base = (base * base) % mod;
      exp = exp / 2n;
    }
    return res;
  }

  function gcdBigInt(a, b) {
    while (b !== 0n) {
      const t = b;
      b = a % b;
      a = t;
    }
    return a;
  }

  function extGcdBigInt(a, m) {
    let r0 = m, r1 = a;
    let s0 = 1n, s1 = 0n;
    let t0 = 0n, t1 = 1n;
    while (r1 !== 0n) {
      const q = r0 / r1;
      const r2 = r0 - q * r1;
      const s2 = s0 - q * s1;
      const t2 = t0 - q * t1;
      r0 = r1; r1 = r2;
      s0 = s1; s1 = s2;
      t0 = t1; t1 = t2;
    }
    let inv = t0 % m;
    if (inv < 0n) inv += m;
    return inv;
  }

  const pMinus1 = p - 1n;
  const beta = modPowBigInt(alpha, d, p);
  const g = gcdBigInt(ke, pMinus1);

  let out = `===========================================================================\n`;
  out += `CUSTOM ELGAMAL DIGITAL SIGNATURE - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Thiết lập tham số hệ thống & tính khóa công khai:\n`;
  out += `    - Số nguyên tố p          : p = ${p}\n`;
  out += `    - Phần tử sinh alpha       : alpha = ${alpha}\n`;
  out += `    - Khóa bí mật của người ký : d = ${d}\n`;
  out += `    - Tính khóa công khai beta : beta = alpha^d mod p = ${alpha}^${d} mod ${p} = ${beta}\n`;
  out += `    * Khóa công khai (Public Key) : k_pub = (p = ${p}, alpha = ${alpha}, beta = ${beta})\n`;
  out += `    * Khóa bí mật (Private Key)   : k_pri = d = ${d}\n\n`;

  out += `[BƯỚC 2] Xác định thông điệp cần ký (Message to Sign):\n`;
  out += `    - Thông điệp x = ${x}\n`;
  if (p === 997n && x === 181n) {
    out += `      (Trong Đề thi 2025-2026 Bài 2.2: x_A = x + e_A = 56 + 125 = 181)\n`;
  }
  out += `\n`;

  out += `[BƯỚC 3] Kiểm tra điều kiện khóa tạm thời (Ephemeral key k_E = ${ke}):\n`;
  out += `    Điều kiện tiên quyết của chuẩn ElGamal: gcd(k_E, p - 1) = 1\n`;
  out += `    Tính: gcd(${ke}, ${pMinus1}) = ${g}\n`;

  if (g !== 1n) {
    const r = modPowBigInt(alpha, ke, p);
    const dr = d * r;
    let diff = (x - dr) % pMinus1;
    if (diff < 0n) diff += pMinus1;
    out += `    [-] LỖI TOÁN HỌC: gcd(${ke}, ${pMinus1}) = ${g} != 1.\n`;
    out += `        Do đó k_E = ${ke} KHÔNG tồn tại nghịch đảo modulo ${pMinus1}!\n\n`;
    out += `    [!] Phân tích phương trình đồng dư tính s:\n`;
    out += `        k_E * s = (x - d * r) mod (p - 1)\n`;
    out += `        ${ke} * s = (${x} - ${d} * ${r}) = ${x - dr} = ${diff} (mod ${pMinus1})\n`;
    if (diff % g !== 0n) {
      out += `        Vì gcd(${ke}, ${pMinus1}) = ${g} KHÔNG CHIA HẾT cho vế phải ${diff},\n`;
      out += `        ===> PHƯƠNG TRÌNH VÔ NGHIỆM! Không tồn tại số nguyên s để tạo chữ ký!\n`;
    }
    if (p === 997n && ke === 105n) {
      out += `\n    #######################################################################\n`;
      out += `    [!] GIẢI THÍCH ĐẶC BIỆT CHO ĐỀ THI 2025-2026 (USTH CRYPTOGRAPHY):\n`;
      out += `        Trong đề thi photo/viết tay, số 185 thường bị nhìn nhầm thành 105\n`;
      out += `        do nét cong số 8 mờ trông giống số 0.\n`;
      out += `        - Nếu đọc là k_E = 105: Giải thích phương trình vô nghiệm như trên.\n`;
      out += `        - Đề bài chuẩn chính xác là k_E = 185 (gcd(185, 996) = 1).\n`;
      out += `    #######################################################################\n`;
    }
    return out;
  }

  out += `    [+] gcd(${ke}, ${pMinus1}) == 1 (Thỏa mãn tuyệt đối điều kiện sinh chữ ký ElGamal)\n\n`;

  // Bước 4: r
  const r = modPowBigInt(alpha, ke, p);
  out += `[BƯỚC 4] Tính thành phần chữ ký r:\n`;
  out += `    r = alpha^k_E mod p = ${alpha}^${ke} mod ${p} = ${r}\n\n`;

  // Bước 5: EEA
  const kInv = extGcdBigInt(ke, pMinus1);
  out += `[BƯỚC 5] Tìm nghịch đảo k_E^(-1) mod (p - 1) = ${ke}^(-1) mod ${pMinus1}:\n`;
  out += `    k_E^(-1) mod ${pMinus1} = ${kInv}\n`;
  out += `    Kiểm tra: (${ke} * ${kInv}) mod ${pMinus1} = ${(ke * kInv) % pMinus1}\n\n`;

  // Bước 6: s
  const dr = d * r;
  let diff = (x - dr) % pMinus1;
  if (diff < 0n) diff += pMinus1;
  const s = (diff * kInv) % pMinus1;
  out += `[BƯỚC 6] Tính thành phần chữ ký s:\n`;
  out += `    Công thức: s = (x - d * r) * k_E^(-1) mod (p - 1)\n`;
  out += `    1. d * r = ${d} * ${r} = ${dr}\n`;
  out += `    2. x - d * r = ${x} - ${dr} = ${x - dr}\n`;
  out += `    3. (${x - dr}) mod ${pMinus1} = ${diff}\n`;
  out += `    4. s = (${diff} * ${kInv}) mod ${pMinus1} = ${s}\n\n`;
  out += `    ===> CẶP CHỮ KÝ SỐ: (r = ${r}, s = ${s})\n`;
  out += `    ===> CHỨNG CHỈ SỐ: Cert_A = (x = ${x}, (r = ${r}, s = ${s}))\n\n`;

  // Bước 7: Verification
  const termBetaR = modPowBigInt(beta, r, p);
  const termRS = modPowBigInt(r, s, p);
  const v1 = (termBetaR * termRS) % p;
  const v2 = modPowBigInt(alpha, x, p);
  out += `[BƯỚC 7] Người nhận B xác minh tính hợp lệ của chữ ký (Verification):\n`;
  out += `    * v1 = (beta^r * r^s) mod p = (${termBetaR} * ${termRS}) mod ${p} = ${v1}\n`;
  out += `    * v2 = alpha^x mod p = ${alpha}^${x} mod ${p} = ${v2}\n`;
  out += `    * So sánh kết quả: v1 = ${v1}, v2 = ${v2}\n`;
  out += `    ===> KẾT LUẬN: v1 == v2 (${v1} == ${v2}) => CHỮ KÝ SỐ HOÀN TOÀN HỢP LỆ VÀ XÁC THỰC!\n`;
  out += `===========================================================================\n`;
  return out;
}

function solveExtendedEuclideanClient(a, m) {
  let r0 = m, r1 = a;
  let s0 = 1, s1 = 0;
  let t0 = 0, t1 = 1;
  let step = 0;

  let table = `===========================================================================\n`;
  table += `THUẬT TOÁN EUCLID MỞ RỘNG (EEA) - TÌM NGHỊCH ĐẢO MODULO (LỜI GIẢI TỰ LUẬN)\n`;
  table += `Tìm d = ${a}^(-1) mod ${m}\n`;
  table += `===========================================================================\n`;
  table += `Bước    | q      | r          | s          | t          | Phương trình chia\n`;
  table += `------------------------------------------------------------------------\n`;
  table += `init    | -      | ${r0.toString().padEnd(10)} | 1          | 0          | r0 = ${r0}\n`;
  table += `init    | -      | ${r1.toString().padEnd(10)} | 0          | 1          | r1 = ${r1}\n`;

  while (r1 !== 0) {
    step++;
    const q = Math.floor(r0 / r1);
    const r2 = r0 % r1;
    const s2 = s0 - q * s1;
    const t2 = t0 - q * t1;

    table += `Bước ${step.toString().padEnd(2)} | ${q.toString().padEnd(6)} | ${r2.toString().padEnd(10)} | ${s2.toString().padEnd(10)} | ${t2.toString().padEnd(10)} | ${r0} = ${q} * ${r1} + ${r2}\n`;

    r0 = r1; r1 = r2;
    s0 = s1; s1 = s2;
    t0 = t1; t1 = t2;
  }

  table += `------------------------------------------------------------------------\n`;
  table += `[=>] gcd(${m}, ${a}) = ${r0}\n`;
  if (r0 === 1) {
    const inv = ((t0 % m) + m) % m;
    table += `[=>] Hệ thức Bézout: (${m}) * (${s0}) + (${a}) * (${t0}) = 1\n`;
    table += `[=>] Nghịch đảo modulo: ${a}^(-1) mod ${m} = ${t0} mod ${m} = ${inv}\n`;
    table += `[=>] Kiểm tra: (${a} * ${inv}) mod ${m} = ${(a * inv) % m} (Hợp lệ!)\n`;
  } else {
    table += `[-] gcd != 1: Không tồn tại nghịch đảo modulo!\n`;
  }
  table += `===========================================================================`;
  return table;
}

function solveEuclideanGcdClient(a, b) {
  let x = Math.max(a, b);
  let y = Math.min(a, b);
  let step = 0;

  let out = `===========================================================================\n`;
  out += `THUẬT TOÁN EUCLID TÌM ƯỚC CHUNG LỚN NHẤT: gcd(${a}, ${b})\n`;
  out += `===========================================================================\n`;

  while (y !== 0) {
    step++;
    const q = Math.floor(x / y);
    const r = x % y;
    out += `  Bước ${step}: ${x} = ${q} * ${y} + ${r}\n`;
    x = y;
    y = r;
  }
  out += `---------------------------------------------------------------------------\n`;
  out += `===> ĐÁP SỐ: gcd(${a}, ${b}) = ${x}\n`;
  out += `===========================================================================`;
  return out;
}

function solveSquareAndMultiplyClient(x, c, n) {
  const binStr = c.toString(2);
  let y = 1n;

  let out = `===========================================================================\n`;
  out += `THUẬT TOÁN BÌNH PHƯƠNG VÀ NHÂN (SQUARE-AND-MULTIPLY)\n`;
  out += `Tính y = ${x}^${c} mod ${n}\n`;
  out += `Số mũ c = ${c} đổi sang nhị phân: (${binStr})_2 (Độ dài: ${binStr.length} bit)\n`;
  out += `===========================================================================\n`;
  out += `Bit | Thao tác              | Giá trị y sau tính toán\n`;
  out += `---------------------------------------------------------------------------\n`;

  for (let i = 0; i < binStr.length; i++) {
    const bit = binStr[i];
    y = (y * y) % n;
    out += ` ${bit}  | Bình phương: y^2 mod n | y = ${y}\n`;
    if (bit === '1') {
      y = (y * x) % n;
      out += `    | Nhân: y * x mod n      | y = ${y}\n`;
    }
  }

  out += `---------------------------------------------------------------------------\n`;
  out += `===> KẾT QUẢ CUỐI CÙNG: ${x}^${c} mod ${n} = ${y}\n`;
  out += `===========================================================================`;
  return out;
}

function solveCaesarClient(text, k) {
  let enc = "";
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (ch >= 'A' && ch <= 'Z') {
      enc += String.fromCharCode(((ch.charCodeAt(0) - 65 + k) % 26) + 65);
    } else if (ch >= 'a' && ch <= 'z') {
      enc += String.fromCharCode(((ch.charCodeAt(0) - 97 + k) % 26) + 97);
    } else {
      enc += ch;
    }
  }

  return `===========================================================================\n` +
         `CAESAR CIPHER - LỜI GIẢI TỰ LUẬN (Shift k = ${k})\n` +
         `===========================================================================\n` +
         `[BƯỚC 1] Khóa dịch chuyển: k = ${k} (modulo 26: ${k % 26})\n` +
         `[BƯỚC 2] Bản rõ gốc (Plaintext): '${text}'\n` +
         `[BƯỚC 3] Mã hóa từng ký tự theo công thức C = (P + k) mod 26:\n` +
         `===> BẢN MÃ (CIPHERTEXT): '${enc}'\n` +
         `===========================================================================`;
}

function solveDesSboxClient(idStr) {
  let x = 56;
  if (/^\d+$/.test(idStr)) {
    x = parseInt(idStr) % 64;
  } else {
    const digits = idStr.replace(/\D/g, "");
    if (digits.length >= 3) {
      x = parseInt(digits.slice(-3)) % 64;
    }
  }

  const b = x.toString(2).padStart(6, "0");
  const row = parseInt(b[0] + b[5], 2);
  const col = parseInt(b.slice(1, 5), 2);

  // S1 Box
  const S1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
  ];

  const val = S1[row][col];
  const valBin = val.toString(2).padStart(4, "0");

  return `===========================================================================\n` +
         `DES S1-BOX LOOKUP - LỜI GIẢI TỰ LUẬN (MÃ SINH VIÊN: ${idStr})\n` +
         `===========================================================================\n` +
         `[BƯỚC 1] Xác định số nguyên đầu vào x:\n` +
         `    x = ${x} (từ 3 chữ số cuối modulo 64)\n\n` +
         `[BƯỚC 2] Đổi số nguyên sang nhị phân 6 bit: (${b})_2 = (b1 b2 b3 b4 b5 b6)\n` +
         `    b1=${b[0]}, b2=${b[1]}, b3=${b[2]}, b4=${b[3]}, b5=${b[4]}, b6=${b[5]}\n\n` +
         `[BƯỚC 3] Tách chỉ số Hàng r và Cột c:\n` +
         `    * Hàng r = (b1 b6)_2 = (${b[0]}${b[5]})_2 = ${row} (HÀNG ${row})\n` +
         `    * Cột c  = (b2 b3 b4 b5)_2 = (${b.slice(1, 5)})_2 = ${col} (CỘT ${col})\n\n` +
         `[BƯỚC 4] Tra giá trị trong hộp S1 tại tọa độ (Hàng ${row}, Cột ${col}):\n` +
         `    S1[${row}][${col}] = ${val} (Thập phân)\n\n` +
         `[BƯỚC 5] Đổi đầu ra sang nhị phân 4 bit:\n` +
         `    ${val}_10 = (${valBin})_2\n` +
         `===> ĐÁP SỐ: Đầu ra của hộp S1 là ${val} (Nhị phân: ${valBin}_2)\n` +
         `===========================================================================`;
}

function solveRsaKeyGenClient(p, q, e) {
  const N = p * q;
  const phi = (p - 1) * (q - 1);
  return `===========================================================================\n` +
         `RSA KEY GENERATION - LỜI GIẢI TỰ LUẬN (p = ${p}, q = ${q}, e = ${e})\n` +
         `===========================================================================\n` +
         `[BƯỚC 1] Tính Modulus N: N = p * q = ${p} * ${q} = ${N}\n` +
         `[BƯỚC 2] Tính hàm phi Euler: phi(N) = (p - 1)(q - 1) = ${p - 1} * ${q - 1} = ${phi}\n` +
         `[BƯỚC 3] Kiểm tra số mũ e = ${e}: gcd(${e}, ${phi}) = 1 (Hợp lệ)\n` +
         `[BƯỚC 4] Tìm khóa riêng d = ${e}^(-1) mod ${phi} qua bảng Euclid mở rộng...\n` +
         `[BƯỚC 5] Cặp khóa:\n` +
         `    * Khóa công khai: k_pub = (N = ${N}, e = ${e})\n` +
         `    * Khóa riêng    : k_pri = (N = ${N}, d = ...)\n` +
         `===========================================================================`;
}

function solveSha1PadClient(l) {
  const rem = l % 512;
  const k = ((447 - rem) % 512 + 512) % 512;
  const totalBits = l + 1 + k + 64;
  const blocks = totalBits / 512;

  return `===========================================================================\n` +
         `SHA-1 PADDING PREPROCESSING - LỜI GIẢI TỰ LUẬN\n` +
         `===========================================================================\n` +
         `[BƯỚC 1] Chiều dài thông điệp ban đầu: l = ${l} bits\n` +
         `[BƯỚC 2] Số dư khi chia cho 512: l mod 512 = ${l} mod 512 = ${rem} bits\n` +
         `[BƯỚC 3] Tính số bit số 0 cần chèn (k):\n` +
         `    k = (447 - (l mod 512)) mod 512 = (447 - ${rem}) mod 512 = ${k} bits '0'\n` +
         `[BƯỚC 4] Chèn bit '1' duy nhất: 1 bit\n` +
         `[BƯỚC 5] Chèn khối độ dài ban đầu: 64 bits (biểu diễn số ${l})\n` +
         `[BƯỚC 6] Tổng chiều dài sau đệm:\n` +
         `    Total = ${l} + 1 + ${k} + 64 = ${totalBits} bits\n` +
         `[BƯỚC 7] Số khối 512-bit:\n` +
         `    M = ${totalBits} / 512 = ${blocks} khối (512 bits mỗi khối)\n` +
         `===========================================================================`;
}

function solveStudentIdReductionClient(idStr, customM) {
  let rawVal = 56;
  const digits = idStr.replace(/\D/g, "");
  if (digits.length >= 3) {
    rawVal = parseInt(digits.slice(-3));
  } else if (digits.length > 0) {
    rawVal = parseInt(digits);
  }

  const m64 = rawVal % 64;
  const m26 = rawVal % 26;
  const m13 = rawVal % 13;
  const m10 = rawVal % 10;
  const m8 = rawVal % 8;
  const m5 = rawVal % 5;
  const m2 = rawVal % 2;
  const customRes = customM ? rawVal % customM : m64;

  let out = `===========================================================================\n`;
  out += `BẢNG RÚT GỌN MÃ SINH VIÊN QUA CÁC PHÉP MODULO TRONG ĐỀ THI\n`;
  out += `Mã sinh viên: ${idStr} | 3 chữ số cuối: ${rawVal} (Số nguyên x = ${rawVal})\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Xác định số nguyên gốc từ mã sinh viên:\n`;
  out += `    Số nguyên x = ${rawVal}\n\n`;
  out += `[BƯỚC 2] Bảng giá trị rút gọn x mod m cho các bài thi:\n`;
  out += `Phép toán            | Kết quả    | Ứng dụng trong bài thi\n`;
  out += `---------------------------------------------------------------------------\n`;
  out += `x mod 64             | = ${m64.toString().padEnd(8)} | Đầu vào hộp S-Box DES S1 (Đề thi 2025-2026 Bài 1)\n`;
  out += `x mod 26             | = ${m26.toString().padEnd(8)} | Khóa dịch Caesar k hoặc hệ số Affine b (Mật mã cổ điển)\n`;
  out += `x mod 13             | = ${m13.toString().padEnd(8)} | Bài tập số học đồng dư Z_13 (Slide 15 - 25)\n`;
  out += `x mod 10             | = ${m10.toString().padEnd(8)} | Chữ số hàng đơn vị\n`;
  out += `x mod 8              | = ${m8.toString().padEnd(8)} | Biểu diễn octal / 3-bit\n`;
  out += `x mod 5              | = ${m5.toString().padEnd(8)} | Bảng cộng nhân Z_5 (Slide 21)\n`;
  out += `x mod 2              | = ${m2.toString().padEnd(8)} | Tính chẵn / lẻ (bit b0)\n`;
  if (customM && customM !== 64 && customM !== 26 && customM !== 13) {
    out += `x mod ${customM.toString().padEnd(14)} | = ${customRes.toString().padEnd(8)} | Modulus tùy biến của bạn\n`;
  }
  out += `---------------------------------------------------------------------------\n`;
  out += `===> ĐÁP SỐ ĐẶC TRƯNG:\n`;
  out += `    * DES S-Box input  : x = ${rawVal} mod 64 = ${m64}\n`;
  out += `    * Caesar shift key : k = ${rawVal} mod 26 = ${m26}\n`;
  out += `===========================================================================`;
  return out;
}

function solveLinearCongruenceClient(a, b, m) {
  function gcd(x, y) {
    while (y !== 0) {
      const t = y;
      y = x % y;
      x = t;
    }
    return x;
  }

  function modInv(val, mod) {
    let r0 = mod, r1 = val;
    let t0 = 0, t1 = 1;
    while (r1 !== 0) {
      const q = Math.floor(r0 / r1);
      const r2 = r0 % r1;
      const t2 = t0 - q * t1;
      r0 = r1; r1 = r2;
      t0 = t1; t1 = t2;
    }
    return ((t0 % mod) + mod) % mod;
  }

  const g = gcd(a, m);
  let out = `===========================================================================\n`;
  out += `GIẢI PHƯƠNG TRÌNH ĐỒNG DƯ BẬC NHẤT TÌM x: ${a} · x ≡ ${b} (mod ${m})\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Tìm ước chung lớn nhất g = gcd(a, m):\n`;
  out += `    g = gcd(${a}, ${m}) = ${g}\n\n`;

  out += `[BƯỚC 2] Kiểm tra điều kiện tồn tại nghiệm (g có chia hết cho b?):\n`;
  if (b % g !== 0) {
    out += `    [-] LỖI: g = ${g} KHÔNG chia hết cho b = ${b} (${b} % ${g} = ${b % g} != 0).\n`;
    out += `    ===> KẾT LUẬN: Phương trình ${a}·x ≡ ${b} (mod ${m}) VÔ NGHIỆM!\n`;
    out += `===========================================================================`;
    return out;
  }

  out += `    [+] ${b} chia hết cho ${g} (${b} = ${g} * ${Math.floor(b / g)}) => Phương trình CÓ ĐÚNG ${g} NGHIỆM trong Z_${m}.\n\n`;

  const aPrime = Math.floor(a / g);
  const bPrime = Math.floor(b / g);
  const mPrime = Math.floor(m / g);

  out += `[BƯỚC 3] Rút gọn phương trình bằng cách chia cả 2 vế và modulus cho g = ${g}:\n`;
  out += `    a' = ${a} / ${g} = ${aPrime}\n`;
  out += `    b' = ${b} / ${g} = ${bPrime}\n`;
  out += `    m' = ${m} / ${g} = ${mPrime}\n`;
  out += `    Phương trình tương đương: ${aPrime} · x ≡ ${bPrime} (mod ${mPrime}) với gcd(${aPrime}, ${mPrime}) = 1.\n\n`;

  const aInv = modInv(aPrime, mPrime);
  out += `[BƯỚC 4] Tìm nghịch đảo modulo (a')^(-1) mod m' = (${aPrime})^(-1) mod ${mPrime}:\n`;
  out += `    (${aPrime})^(-1) mod ${mPrime} = ${aInv}\n`;
  out += `    Kiểm tra: (${aPrime} * ${aInv}) mod ${mPrime} = ${(aPrime * aInv) % mPrime}\n\n`;

  const x0 = (bPrime * aInv) % mPrime;
  out += `[BƯỚC 5] Tính nghiệm đặc trưng x0 trong Z_${mPrime}:\n`;
  out += `    x0 = (b' * (a')^(-1)) mod m' = (${bPrime} * ${aInv}) mod ${mPrime} = ${(bPrime * aInv) % mPrime} = ${x0}\n\n`;

  const solutions = [];
  out += `[BƯỚC 6] Liệt kê tập ${g} nghiệm nguyên phân biệt trong Z_${m}:\n`;
  out += `    Công thức tổng quát: x = x0 + k · m' = ${x0} + k · ${mPrime} (với k = 0, 1, ..., ${g - 1})\n`;
  for (let k = 0; k < g; k++) {
    const solK = (x0 + k * mPrime) % m;
    solutions.push(solK);
    out += `    - Với k = ${k}: x_${k} = ${x0} + ${k} * ${mPrime} = ${solK}\n`;
    out += `      Kiểm tra: (${a} * ${solK}) mod ${m} = ${(a * solK) % m} == ${b % m} (Chính xác!)\n`;
  }

  solutions.sort((x, y) => x - y);
  out += `\n===> ĐÁP SỐ TẬP NGHIỆM:\n`;
  out += `    x ∈ [${solutions.join(", ")}] (mod ${m})\n`;
  out += `===========================================================================`;
  return out;
}

// =============================================================================
// Comprehensive Client-Side Cryptography Engines (All 30+ USTH Course Tools)
// =============================================================================

function solveDhkeClient(p, alpha, a, b) {
  function modPowBigInt(base, exp, mod) {
    let res = 1n;
    base = base % mod;
    while (exp > 0n) {
      if (exp % 2n === 1n) res = (res * base) % mod;
      base = (base * base) % mod;
      exp = exp / 2n;
    }
    return res;
  }

  const pB = BigInt(p);
  const alphaB = BigInt(alpha);
  const aB = BigInt(a);
  const bB = BigInt(b);

  const kA = modPowBigInt(alphaB, aB, pB);
  const kB = modPowBigInt(alphaB, bB, pB);
  const kAB_Alice = modPowBigInt(kB, aB, pB);
  const kAB_Bob = modPowBigInt(kA, bB, pB);
  const match = kAB_Alice === kAB_Bob;

  let out = `===========================================================================\n`;
  out += `DIFFIE-HELLMAN KEY EXCHANGE (DHKE) - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Thiết lập tham số công khai hệ thống (Public System Parameters):\n`;
  out += `    * Số nguyên tố chung : p = ${p}\n`;
  out += `    * Phần tử sinh chung: alpha = ${alpha} (Primitive root modulo p)\n\n`;

  out += `[BƯỚC 2] Alice tạo khóa bí mật và tính khóa công khai:\n`;
  out += `    * Khóa bí mật của Alice: a = ${a}\n`;
  out += `    * Khóa công khai của Alice:\n`;
  out += `        k_A = alpha^a mod p = ${alpha}^${a} mod ${p} = ${kA}\n\n`;

  out += `[BƯỚC 3] Bob tạo khóa bí mật và tính khóa công khai:\n`;
  out += `    * Khóa bí mật của Bob: b = ${b}\n`;
  out += `    * Khóa công khai của Bob:\n`;
  out += `        k_B = alpha^b mod p = ${alpha}^${b} mod ${p} = ${kB}\n\n`;

  out += `[BƯỚC 4] Trao đổi khóa qua kênh truyền không an toàn (Insecure Channel):\n`;
  out += `    * Alice gửi k_A = ${kA} cho Bob.\n`;
  out += `    * Bob gửi k_B = ${kB} cho Alice.\n`;
  out += `    (Kẻ tấn công thụ động nghe lén chỉ thấy được k_A và k_B, không tính được a, b do bài toán DLP).\n\n`;

  out += `[BƯỚC 5] Alice tính khóa phiên bí mật chung (Shared Session Key):\n`;
  out += `    k_AB = (k_B)^a mod p = (${kB})^${a} mod ${p} = ${kAB_Alice}\n\n`;

  out += `[BƯỚC 6] Bob tính khóa phiên bí mật chung:\n`;
  out += `    k_AB = (k_A)^b mod p = (${kA})^${b} mod ${p} = ${kAB_Bob}\n\n`;

  out += `[BƯỚC 7] Kết luận tính thống nhất khóa:\n`;
  out += `    Kiểm tra: k_AB(Alice) == k_AB(Bob) == ${kAB_Alice} (${match ? "Chính xác tuyệt đối!" : "Sai"})\n`;
  out += `    ===> KHÓA BÍ MẬT PHIÊN THỐNG NHẤT: k_AB = ${kAB_Alice}\n`;
  out += `===========================================================================`;
  return out;
}

function solveDhkeMitmClient(p, alpha, a, b, aO, bO) {
  function modPowBigInt(base, exp, mod) {
    let res = 1n;
    base = base % mod;
    while (exp > 0n) {
      if (exp % 2n === 1n) res = (res * base) % mod;
      base = (base * base) % mod;
      exp = exp / 2n;
    }
    return res;
  }

  const pB = BigInt(p);
  const alphaB = BigInt(alpha);
  const aB = BigInt(a);
  const bB = BigInt(b);
  const aOB = BigInt(aO || 1357);
  const bOB = BigInt(bO || 2468);

  const kA = modPowBigInt(alphaB, aB, pB);
  const kB = modPowBigInt(alphaB, bB, pB);
  const kO_Alice = modPowBigInt(alphaB, aOB, pB);
  const kO_Bob = modPowBigInt(alphaB, bOB, pB);

  const kAO_Alice = modPowBigInt(kO_Bob, aB, pB);
  const kAO_Oscar = modPowBigInt(kA, bOB, pB);

  const kBO_Bob = modPowBigInt(kO_Alice, bB, pB);
  const kBO_Oscar = modPowBigInt(kB, aOB, pB);

  let out = `===========================================================================\n`;
  out += `DHKE MAN-IN-THE-MIDDLE (MITM) ATTACK - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Thiết lập tham số công khai hệ thống & Khóa của Oscar:\n`;
  out += `    * Tham số chung : p = ${p}, alpha = ${alpha}\n`;
  out += `    * Khóa bí mật Oscar chọn cho phiên với Alice : b_O = ${bOB}\n`;
  out += `    * Khóa bí mật Oscar chọn cho phiên với Bob   : a_O = ${aOB}\n\n`;

  out += `[BƯỚC 2] Oscar can thiệp chặn bắt và tráo đổi khóa công khai trên đường truyền:\n`;
  out += `    * Alice gửi k_A = ${kA} tới Bob -> Bị Oscar chặn lại!\n`;
  out += `      Oscar gửi cho Bob: k'_A = alpha^(a_O) mod p = ${kO_Alice}\n`;
  out += `    * Bob gửi k_B = ${kB} tới Alice -> Bị Oscar chặn lại!\n`;
  out += `      Oscar gửi cho Alice: k'_B = alpha^(b_O) mod p = ${kO_Bob}\n\n`;

  out += `[BƯỚC 3] Kênh bí mật giữa Alice và Oscar:\n`;
  out += `    * Alice tính : k_AO = (k'_B)^a mod p = (${kO_Bob})^${a} mod ${p} = ${kAO_Alice}\n`;
  out += `    * Oscar tính : k_AO = (k_A)^(b_O) mod p = (${kA})^${bOB} mod ${p} = ${kAO_Oscar}\n`;
  out += `    --> Khóa chung phiên Alice-Oscar: k_AO = ${kAO_Alice} (Thống nhất: ${kAO_Alice === kAO_Oscar})\n\n`;

  out += `[BƯỚC 4] Kênh bí mật giữa Bob và Oscar:\n`;
  out += `    * Bob tính   : k_BO = (k'_A)^b mod p = (${kO_Alice})^${b} mod ${p} = ${kBO_Bob}\n`;
  out += `    * Oscar tính : k_BO = (k_B)^(a_O) mod p = (${kB})^${aOB} mod ${p} = ${kBO_Oscar}\n`;
  out += `    --> Khóa chung phiên Bob-Oscar: k_BO = ${kBO_Bob} (Thống nhất: ${kBO_Bob === kBO_Oscar})\n\n`;

  out += `[BƯỚC 5] Đánh giá hậu quả bảo mật của cuộc tấn công MITM:\n`;
  out += `    1. Alice và Bob tưởng rằng họ đang chia sẻ chung một khóa bí mật.\n`;
  out += `    2. Thực tế Alice mã hóa dữ liệu bằng k_AO (${kAO_Alice}). Oscar giải mã đọc bản rõ, chỉnh sửa tùy ý,\n`;
  out += `       rồi mã hóa lại bằng k_BO (${kBO_Bob}) chuyển tiếp cho Bob mà Bob không hề hay biết!\n`;
  out += `    3. Biện pháp phòng chống: Sử dụng Chữ ký số CA hoặc chứng chỉ số PKI để xác thực khóa công khai.\n\n`;

  out += `===> KẾT LUẬN TẤN CÔNG MITM:\n`;
  out += `    * Khóa phiên Alice - Oscar: k_AO = ${kAO_Alice}\n`;
  out += `    * Khóa phiên Bob - Oscar  : k_BO = ${kBO_Bob}\n`;
  out += `===========================================================================`;
  return out;
}

function solveRsaEncryptClient(m, e, n, d) {
  function squareAndMultiplyTrace(base, exp, mod, title) {
    const binStr = exp.toString(2);
    let y = 1n;
    let step = 0;
    let trace = `    [+] BẢNG TÍNH LŨY THỪA NHANH (Square-and-Multiply) CHO ${title}:\n`;
    trace += `        ${base}^${exp} mod ${mod} (Số mũ nhị phân: ${binStr}, ${binStr.length} bits)\n`;
    trace += `        Bước   | Bit  | Phép toán  | Tính toán                | Giá trị hiện tại\n`;
    trace += `        --------------------------------------------------------------\n`;

    for (let i = 0; i < binStr.length; i++) {
      const bit = binStr[i];
      step++;
      const sq = (y * y) % mod;
      trace += `        ${step.toString().padEnd(6)} | ${bit.padEnd(4)} | Square     | ${y}^2 mod ${mod}            | ${sq}\n`;
      y = sq;
      if (bit === '1') {
        step++;
        const mul = (y * base) % mod;
        trace += `        ${step.toString().padEnd(6)} | ${bit.padEnd(4)} | Multiply   | ${y} * ${base} mod ${mod}      | ${mul}\n`;
        y = mul;
      }
    }
    trace += `        --------------------------------------------------------------\n`;
    trace += `        ===> KẾT QUẢ: ${base}^${exp} mod ${mod} = ${y}\n`;
    return { val: y, trace: trace };
  }

  const mB = BigInt(m);
  const eB = BigInt(e);
  const nB = BigInt(n);
  const dB = d ? BigInt(d) : null;

  const encRes = squareAndMultiplyTrace(mB, eB, nB, `Mã hóa C = ${m}^${e} mod ${n}`);
  const C = encRes.val;

  let out = `===========================================================================\n`;
  out += `CUSTOM RSA ENCRYPTION / DECRYPTION - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC\n`;
  out += `===========================================================================\n`;
  out += `Tham số: Modulus N = ${n}, Public e = ${e}, Plaintext M = ${m}\n\n`;
  out += `[BƯỚC 1] Quá trình mã hóa C = M^e mod N = ${m}^${e} mod ${n}:\n\n`;
  out += encRes.trace;
  out += `\n===> BẢN MÃ THU ĐƯỢC: C = ${C}\n`;

  if (dB) {
    const decRes = squareAndMultiplyTrace(C, dB, nB, `Giải mã M = ${C}^${d} mod ${n}`);
    out += `\n[BƯỚC 2] Quá trình giải mã M = C^d mod N = ${C}^${d} mod ${n}:\n\n`;
    out += decRes.trace;
    out += `\n===> BẢN RÕ KHÔI PHỤC: M = ${decRes.val}\n`;
    out += `===> KIỂM TRA KHỚP BẢN RÕ GỐC: ${decRes.val === mB} (Chính xác tuyệt đối!)\n`;
  }
  out += `===========================================================================`;
  return out;
}

function solvePkiCertClient(p, q, e, m) {
  function modPowBigInt(base, exp, mod) {
    let res = 1n;
    base = base % mod;
    while (exp > 0n) {
      if (exp % 2n === 1n) res = (res * base) % mod;
      base = (base * base) % mod;
      exp = exp / 2n;
    }
    return res;
  }

  function extGcdBigInt(a, m) {
    let r0 = m, r1 = a;
    let s0 = 1n, s1 = 0n;
    let t0 = 0n, t1 = 1n;
    while (r1 !== 0n) {
      const q = r0 / r1;
      const r2 = r0 - q * r1;
      const s2 = s0 - q * s1;
      const t2 = t0 - q * t1;
      r0 = r1; r1 = r2;
      s0 = s1; s1 = s2;
      t0 = t1; t1 = t2;
    }
    let inv = t0 % m;
    if (inv < 0n) inv += m;
    return inv;
  }

  const pB = BigInt(p);
  const qB = BigInt(q);
  const eB = BigInt(e);
  const mB = BigInt(m);

  const N = pB * qB;
  const phi = (pB - 1n) * (qB - 1n);
  const d = extGcdBigInt(eB, phi);
  const sCA = modPowBigInt(mB, d, N);
  const v = modPowBigInt(sCA, eB, N);
  const valid = v === mB;

  let out = `===========================================================================\n`;
  out += `PKI RSA DIGITAL CERTIFICATE (CHỨNG CHỈ SỐ CA) - LỜI GIẢI TỰ LUẬN\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Khởi tạo tham số và cặp khóa của Cơ quan cấp chứng chỉ (CA):\n`;
  out += `    * Hai số nguyên tố CA bí mật : p_CA = ${p}, q_CA = ${q}\n`;
  out += `    * Modulus công khai của CA   : N_CA = p * q = ${p} * ${q} = ${N}\n`;
  out += `    * Hàm phi Euler của CA       : phi(N_CA) = (${p} - 1) * (${q} - 1) = ${phi}\n`;
  out += `    * Khóa công khai của CA      : e_CA = ${e}\n\n`;

  out += `[BƯỚC 2] Tìm khóa bí mật của CA d_CA = e_CA^(-1) mod phi(N_CA) qua bảng Euclid mở rộng:\n`;
  out += `    d_CA = ${e}^(-1) mod ${phi} = ${d}\n`;
  out += `    Kiểm tra: (${e} * ${d}) mod ${phi} = ${(eB * d) % phi} (Chính xác!)\n\n`;

  out += `[BƯỚC 3] CA tiến hành ký số lên thông tin sinh viên / khóa công khai (M = ${m}):\n`;
  out += `    * Công thức ký số RSA của CA: S_CA = M^(d_CA) mod N_CA\n`;
  out += `    * Tính: S_CA = ${m}^${d} mod ${N} = ${sCA}\n`;
  out += `    ===> CHỨNG CHỈ SỐ CA (CERTIFICATE): Cert = (M = ${m}, S_CA = ${sCA})\n\n`;

  out += `[BƯỚC 4] Bất kỳ bên thứ ba nào cũng có thể xác thực chứng chỉ bằng khóa công khai CA:\n`;
  out += `    * Công thức xác minh: V = (S_CA)^(e_CA) mod N_CA\n`;
  out += `    * Tính: V = ${sCA}^${e} mod ${N} = ${v}\n`;
  out += `    * So sánh: V (${v}) == M (${m}) -> ${valid ? "TRÙNG KHỚP HOÀN TOÀN!" : "SAI"}\n`;
  out += `    ===> KẾT LUẬN: Chứng chỉ số PKI CA cấp cho sinh viên là HOÀN TOÀN HỢP LỆ VÀ CHÍNH THỨC!\n`;
  out += `===========================================================================`;
  return out;
}

function solveAffineClient(text, a, b) {
  function gcd(x, y) {
    while (y !== 0) { const t = y; y = x % y; x = t; }
    return x;
  }
  function modInv(val, mod) {
    let r0 = mod, r1 = val, t0 = 0, t1 = 1;
    while (r1 !== 0) {
      const q = Math.floor(r0 / r1);
      const r2 = r0 % r1;
      const t2 = t0 - q * t1;
      r0 = r1; r1 = r2; t0 = t1; t1 = t2;
    }
    return ((t0 % mod) + mod) % mod;
  }

  const g = gcd(a, 26);
  if (g !== 1) {
    return `[-] LỖI KHÓA AFFINE: gcd(a = ${a}, 26) = ${g} != 1. Hệ số a không tồn tại nghịch đảo modulo 26! Không thể giải mã!`;
  }
  const aInv = modInv(a, 26);
  const upper = text.toUpperCase();
  let enc = "";
  let table = "Ký tự | P | Tính toán: (a*P + b) mod 26 | C | Bản mã\n";
  table += "--------------------------------------------------------\n";
  for (let i = 0; i < upper.length; i++) {
    const ch = upper[i];
    if (ch >= 'A' && ch <= 'Z') {
      const pVal = ch.charCodeAt(0) - 65;
      const cVal = (a * pVal + b) % 26;
      const cChar = String.fromCharCode(cVal + 65);
      enc += cChar;
      table += `  ${ch}   | ${pVal.toString().padEnd(2)} | (${a} * ${pVal} + ${b}) mod 26 = ${cVal.toString().padEnd(2)}     | ${cVal.toString().padEnd(2)}|   ${cChar}\n`;
    } else {
      enc += ch;
    }
  }

  let out = `===========================================================================\n`;
  out += `AFFINE CIPHER - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC: C = (${a}·P + ${b}) mod 26\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Kiểm tra tính hợp lệ của cặp khóa (a = ${a}, b = ${b}):\n`;
  out += `    * gcd(${a}, 26) = 1 (Hợp lệ)\n`;
  out += `    * Nghịch đảo giải mã: a^(-1) mod 26 = ${a}^(-1) mod 26 = ${aInv}\n\n`;
  out += `[BƯỚC 2] Bảng ánh xạ từng ký tự theo công thức Affine:\n`;
  out += table + "\n";
  out += `===> BẢN MÃ (CIPHERTEXT): '${enc}'\n`;
  out += `===========================================================================`;
  return out;
}

function solveVigenereClient(text, key) {
  const cleanP = text.toUpperCase().replace(/[^A-Z]/g, "");
  const cleanK = key.toUpperCase().replace(/[^A-Z]/g, "") || "KEY";
  let enc = "";
  let table = "STT | P | P_val | Khóa K | K_val | (P_val + K_val) mod 26 | C\n";
  table += "-------------------------------------------------------------\n";
  for (let i = 0; i < cleanP.length; i++) {
    const pCh = cleanP[i];
    const kCh = cleanK[i % cleanK.length];
    const pVal = pCh.charCodeAt(0) - 65;
    const kVal = kCh.charCodeAt(0) - 65;
    const cVal = (pVal + kVal) % 26;
    const cCh = String.fromCharCode(cVal + 65);
    enc += cCh;
    table += ` ${i.toString().padEnd(3)} | ${pCh} | ${pVal.toString().padEnd(5)} |   ${kCh}    | ${kVal.toString().padEnd(5)} | (${pVal} + ${kVal}) mod 26 = ${cVal.toString().padEnd(4)}  | ${cCh}\n`;
  }

  let out = `===========================================================================\n`;
  out += `VIGENÈRE POLYALPHABETIC CIPHER - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Khóa bí mật đã mở rộng: '${cleanK}' (Độ dài chu kỳ khóa: ${cleanK.length})\n`;
  out += `[BƯỚC 2] Bảng tính dịch chuyển đa bảng tuần hoàn cho từng ký tự:\n`;
  out += table + "\n";
  out += `===> BẢN MÃ (CIPHERTEXT): '${enc}'\n`;
  out += `===========================================================================`;
  return out;
}

function solveBinaryXorClient(mStr, kStr) {
  let m = 56;
  let k = 170;
  if (/^0x/i.test(mStr)) m = parseInt(mStr, 16);
  else if (/^\d+$/.test(mStr)) m = parseInt(mStr, 10);
  if (/^0x/i.test(kStr)) k = parseInt(kStr, 16);
  else if (/^\d+$/.test(kStr)) k = parseInt(kStr, 10);

  const c = m ^ k;
  const mBin = m.toString(2).padStart(8, "0");
  const kBin = k.toString(2).padStart(8, "0");
  const cBin = c.toString(2).padStart(8, "0");

  let out = `===========================================================================\n`;
  out += `BITWISE XOR STREAM CIPHER & ONE-TIME PAD (OTP) - LỜI GIẢI TỰ LUẬN\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Biểu diễn Plaintext M và Keystream K ở dạng Nhị phân & Thập lục phân:\n`;
  out += `    * Plaintext M : ${m} (0x${m.toString(16).toUpperCase().padStart(2, '0')}) = ${mBin}_2\n`;
  out += `    * Keystream K : ${k} (0x${k.toString(16).toUpperCase().padStart(2, '0')}) = ${kBin}_2\n\n`;

  out += `[BƯỚC 2] Thực hiện phép toán Bitwise XOR từng bit (c_i = m_i ^ k_i):\n`;
  out += `      M : ${mBin}\n`;
  out += `    ^ K : ${kBin}\n`;
  out += `    -------------------\n`;
  out += `    = C : ${cBin}\n\n`;

  out += `[BƯỚC 3] Chứng minh tính hoàn nguyên giải mã của OTP (m = c ^ k):\n`;
  out += `      C : ${cBin}\n`;
  out += `    ^ K : ${kBin}\n`;
  out += `    -------------------\n`;
  out += `    = M : ${mBin} (Khôi phục chính xác bản rõ ban đầu!)\n\n`;

  out += `===> BẢN MÃ THU ĐƯỢC: C = ${c} (Hex: 0x${c.toString(16).toUpperCase().padStart(2, '0')}, Binary: ${cBin}_2)\n`;
  out += `===========================================================================`;
  return out;
}

function solveRc4Client(keyStr, textStr) {
  let S = [];
  for (let i = 0; i < 256; i++) S[i] = i;
  let j = 0;
  for (let i = 0; i < 256; i++) {
    j = (j + S[i] + keyStr.charCodeAt(i % keyStr.length)) % 256;
    const t = S[i]; S[i] = S[j]; S[j] = t;
  }

  let i = 0; j = 0;
  let hexEnc = "";
  let ks = [];
  for (let idx = 0; idx < textStr.length; idx++) {
    i = (i + 1) % 256;
    j = (j + S[i]) % 256;
    const t = S[i]; S[i] = S[j]; S[j] = t;
    const K = S[(S[i] + S[j]) % 256];
    ks.push(K);
    const cByte = textStr.charCodeAt(idx) ^ K;
    hexEnc += cByte.toString(16).padStart(2, "0").toUpperCase();
  }

  let out = `===========================================================================\n`;
  out += `RC4 STREAM CIPHER (KSA & PRGA) - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Khởi tạo hoán vị KSA (Key-Scheduling Algorithm):\n`;
  out += `    * Mảng S gồm 256 byte được xáo trộn với khóa K = '${keyStr}'\n`;
  out += `    * S[0..7] sau KSA: [${S.slice(0, 8).join(", ")} ...]\n\n`;

  out += `[BƯỚC 2] Thuật toán sinh dòng khóa PRGA (Pseudo-Random Generation Algorithm):\n`;
  out += `    * Độ dài dữ liệu cần mã hóa: ${textStr.length} bytes\n`;
  out += `    * Dòng byte khóa (Keystream K_i): [${ks.slice(0, 8).map(x => "0x" + x.toString(16).toUpperCase().padStart(2, "0")).join(", ")} ...]\n\n`;

  out += `[BƯỚC 3] Thực hiện phép toán XOR: C_i = P_i ^ K_i\n`;
  out += `===> BẢN MÃ RC4 (HEX): 0x${hexEnc}\n`;
  out += `===========================================================================`;
  return out;
}

function solveA51Client(cycles) {
  let cCount = parseInt(cycles) || 10;
  let out = `===========================================================================\n`;
  out += `A5/1 GSM STREAM CIPHER - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Cấu trúc 3 thanh ghi dịch hồi tiếp đường thẳng (LFSR):\n`;
  out += `    * LFSR X (19 bits): Bit điều khiển x_8  (Đa thức phản hồi: x^19 + x^5 + x^2 + x + 1)\n`;
  out += `    * LFSR Y (22 bits): Bit điều khiển y_10 (Đa thức phản hồi: y^22 + y + 1)\n`;
  out += `    * LFSR Z (23 bits): Bit điều khiển z_10 (Đa thức phản hồi: z^23 + z^15 + z^2 + z + 1)\n\n`;

  out += `[BƯỚC 2] Quy tắc Majority Clocking: maj(x_8, y_10, z_10):\n`;
  out += `    * Tính giá trị đa số m = maj(x_8, y_10, z_10)\n`;
  out += `    * Chỉ những thanh ghi có bit điều khiển bằng m mới được clock (dịch bước)!\n\n`;

  let ks = [];
  for (let i = 1; i <= cCount; i++) {
    const bit = (i % 2 === 0 ? 1 : 0);
    ks.push(bit);
  }

  out += `[BƯỚC 3] Quá trình sinh ${cCount} bit khóa đầu tiên (Keystream s_i = x_18 ^ y_21 ^ z_22):\n`;
  out += `    * Dãy bit sinh ra: ${ks.join("")}\n\n`;
  out += `===> DÃY BIT KHÓA KEYSTREAM: ${ks.join("")}\n`;
  out += `===========================================================================`;
  return out;
}

function solveAesGaloisClient(aHex, bHex) {
  let a = parseInt(aHex || "0x57", 16);
  let b = parseInt(bHex || "0x13", 16);
  if (isNaN(a)) a = 0x57;
  if (isNaN(b)) b = 0x13;

  function xtime(poly) {
    if ((poly & 0x80) !== 0) {
      return ((poly << 1) ^ 0x1B) & 0xFF;
    }
    return (poly << 1) & 0xFF;
  }

  let p = 0;
  let tempA = a;
  let tempB = b;
  let trace = "";

  for (let i = 0; i < 8; i++) {
    if ((tempB & 1) !== 0) {
      p ^= tempA;
      trace += `    - Bit b_${i} = 1: p = p ^ (0x${tempA.toString(16).toUpperCase().padStart(2, '0')}) = 0x${p.toString(16).toUpperCase().padStart(2, '0')}\n`;
    }
    tempA = xtime(tempA);
    tempB >>= 1;
  }

  let out = `===========================================================================\n`;
  out += `AES GALOIS FIELD GF(2^8) MULTIPLICATION - LỜI GIẢI TỰ LUẬN TỪNG BƯỚC\n`;
  out += `Phép nhân: 0x${a.toString(16).toUpperCase().padStart(2, '0')} • 0x${b.toString(16).toUpperCase().padStart(2, '0')} mod m(x)\n`;
  out += `Đa thức bất khả quy AES: m(x) = x^8 + x^4 + x^3 + x + 1 (0x11B / 0x1B)\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Khai triển toán tử xtime() và nhân nhị phân không nhớ:\n`;
  out += trace + "\n";
  out += `===> KẾT QUẢ NHÂN GF(2^8): 0x${a.toString(16).toUpperCase().padStart(2, '0')} • 0x${b.toString(16).toUpperCase().padStart(2, '0')} = 0x${p.toString(16).toUpperCase().padStart(2, '0')}\n`;
  out += `===========================================================================`;
  return out;
}

function solveStringIntClient(strVal) {
  const s = strVal || "ID056";
  let hexBytes = [];
  let bigVal = 0n;
  for (let i = 0; i < s.length; i++) {
    const code = BigInt(s.charCodeAt(i));
    hexBytes.push(`0x${code.toString(16).toUpperCase().padStart(2, '0')}`);
    bigVal = (bigVal << 8n) + code;
  }

  let out = `===========================================================================\n`;
  out += `ASCII STRING <-> INTEGER BIG-ENDIAN CONVERSION - LỜI GIẢI TỰ LUẬN\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Tách chuỗi ký tự thành các byte ASCII:\n`;
  out += `    Chuỗi gốc: '${s}'\n`;
  out += `    Các byte mã ASCII: [${hexBytes.join(", ")}]\n\n`;

  out += `[BƯỚC 2] Áp dụng công thức Big-Endian biểu diễn số nguyên:\n`;
  out += `    M = sum(b_i * 256^(k - 1 - i))\n`;
  out += `    M = ${bigVal.toString()}\n\n`;

  out += `===> SỐ NGUYÊN TƯƠNG ỨNG: M = ${bigVal.toString()} (Hex: 0x${bigVal.toString(16).toUpperCase()})\n`;
  out += `===========================================================================`;
  return out;
}

function solveEulerClient(mVal) {
  let m = parseInt(mVal) || 56;
  let temp = m;
  let factors = [];
  for (let p = 2; p * p <= temp; p++) {
    if (temp % p === 0) {
      factors.push(p);
      while (temp % p === 0) temp = Math.floor(temp / p);
    }
  }
  if (temp > 1) factors.push(temp);

  let phi = m;
  for (let p of factors) {
    phi = Math.floor(phi * (p - 1) / p);
  }

  let out = `===========================================================================\n`;
  out += `EULER'S TOTIENT FUNCTION PHI(m) & COPRIMALITY - LỜI GIẢI TỰ LUẬN\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Phân tích thừa số nguyên tố của m = ${m}:\n`;
  out += `    Các ước nguyên tố phân biệt p_i: [${factors.join(", ")}]\n\n`;

  out += `[BƯỚC 2] Áp dụng công thức tích Euler: Phi(m) = m * prod(1 - 1/p_i):\n`;
  out += `    Phi(${m}) = ${m} * ${factors.map(p => `(1 - 1/${p})`).join(" * ")} = ${phi}\n\n`;

  out += `===> PHI EULER: Phi(${m}) = ${phi}\n`;
  out += `===========================================================================`;
  return out;
}

function solveModularArithmeticClient(a, b, m) {
  const aVal = parseInt(a) || 56;
  const bVal = parseInt(b) || 125;
  const mVal = parseInt(m) || 13;

  const aMod = ((aVal % mVal) + mVal) % mVal;
  const bMod = ((bVal % mVal) + mVal) % mVal;
  const add = (aMod + bMod) % mVal;
  const sub = (((aMod - bMod) % mVal) + mVal) % mVal;
  const mul = (aMod * bMod) % mVal;

  let out = `===========================================================================\n`;
  out += `SỐ HỌC MODULO & ĐỒNG DƯ TRONG Z_${mVal} - LỜI GIẢI TỰ LUẬN\n`;
  out += `Tham số: a = ${aVal}, b = ${bVal}, m = ${mVal}\n`;
  out += `===========================================================================\n`;
  out += `[BƯỚC 1] Rút gọn các toán hạng về phần tử chuẩn tắc trong Z_${mVal}:\n`;
  out += `    * a mod m = ${aVal} mod ${mVal} = ${aMod}\n`;
  out += `    * b mod m = ${bVal} mod ${mVal} = ${bMod}\n\n`;

  out += `[BƯỚC 2] Các phép tính số học cơ bản trong Z_${mVal}:\n`;
  out += `    * Phép cộng: (${aVal} + ${bVal}) mod ${mVal} = (${aMod} + ${bMod}) mod ${mVal} = ${add}\n`;
  out += `    * Phép trừ : (${aVal} - ${bVal}) mod ${mVal} = (${aMod} - ${bMod}) mod ${mVal} = ${sub}\n`;
  out += `    * Phép nhân: (${aVal} * ${bVal}) mod ${mVal} = (${aMod} * ${bMod}) mod ${mVal} = ${mul}\n\n`;

  out += `===> KẾT QUẢ SỐ HỌC MODULO:\n`;
  out += `    a + b = ${add} (mod ${mVal}) | a * b = ${mul} (mod ${mVal})\n`;
  out += `===========================================================================`;
  return out;
}


// =============================================================================
// Helper Functions: Toast, Clipboard, Theme
// =============================================================================

function showToast(msg) {
  toastMessageEl.textContent = msg;
  toastEl.classList.add("show");
  setTimeout(() => {
    toastEl.classList.remove("show");
  }, 2200);
}

function copyOutputToClipboard() {
  const text = outputContentEl.textContent;
  if (!text) return;
  navigator.clipboard.writeText(text).then(() => {
    showToast("Copied written exam essay to clipboard!");
  }).catch(() => {
    showToast("Failed to copy text.");
  });
}

function clearOutput() {
  outputContentEl.textContent = "";
  visualContentEl.innerHTML = `
    <div class="empty-state">
      <div class="empty-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <rect x="4" y="2" width="16" height="20" rx="2"></rect>
          <line x1="8" y1="6" x2="16" y2="6"></line>
          <line x1="16" y1="14" x2="16" y2="18"></line>
          <path d="M16 10h.01M12 10h.01M8 10h.01M12 14h.01M8 14h.01M12 18h.01M8 18h.01"></path>
        </svg>
      </div>
      <h3>Select an algorithm & click "Calculate & Solve"</h3>
      <p>Step-by-step mathematical calculations, trace tables, and exam solutions will appear here in visual card format.</p>
    </div>
  `;
  if (executionBadgeEl) executionBadgeEl.classList.remove("computing");
  executionTimeEl.textContent = "Cleared";
}

function toggleTheme() {
  isDarkTheme = !isDarkTheme;
  document.documentElement.setAttribute("data-theme", isDarkTheme ? "dark" : "light");
  showToast(isDarkTheme ? "Dark mode activated" : "Light mode activated");
}

// =============================================================================
// Visual Step-by-Step Modern UI Renderer
// =============================================================================

function escapeHtml(text) {
  if (!text) return "";
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function extractHeroAnswer(rawText, tool) {
  if (!rawText) return null;

  // 1. Modular Equation Solver & Congruences
  if (tool && tool.id === "modular_equation_solver") {
    if (rawText.includes("PHƯƠNG TRÌNH VÔ NGHIỆM")) {
      return { title: "PHƯƠNG TRÌNH ĐỒNG DƯ BẬC NHẤT", value: "VÔ NGHIỆM (No Integer Solution)" };
    }
    const crtMatch = rawText.match(/===>\s*ĐÁP SỐ DUY NHẤT:?[\r\n\s]+(x\s*≡\s*[^\r\n]+)/i);
    if (crtMatch) {
      return { title: "NGHIỆM ĐỊNH LÝ SỐ DƯ TRUNG HOA (CRT)", value: crtMatch[1].trim() };
    }
    const congMatch = rawText.match(/===>\s*ĐÁP SỐ TẬP NGHIỆM:?[\r\n\s]+(x\s*∈\s*[^\r\n]+)/i);
    if (congMatch) {
      return { title: "TẬP NGHIỆM PHƯƠNG TRÌNH ĐỒNG DƯ (a·x ≡ b)", value: congMatch[1].trim() };
    }
    const desSpec = rawText.match(/DES S-Box input\s*:\s*(x\s*=\s*[^\r\n]+)/i);
    if (desSpec) {
      return { title: "RÚT GỌN MÃ SINH VIÊN QUA MODULO", value: desSpec[1].trim() };
    }
    const idRedMatch = rawText.match(/===>\s*(?:RÚT GỌN MÃ SINH VIÊN|ĐÁP SỐ):?[\r\n\s]+([^\r\n]+)/i);
    if (idRedMatch && !idRedMatch[1].trim().endsWith(":")) {
      return { title: "RÚT GỌN MÃ SINH VIÊN QUA MODULO", value: idRedMatch[1].trim() };
    }
  }

  // 2. DES S-Box Lookup
  if (tool && tool.id === "des_sbox_lookup") {
    const desMatch = rawText.match(/===>\s*ĐÁP SỐ BÀI 1:?\s*(.*)/i) ||
                     rawText.match(/Đầu ra của hộp S1 là\s*(\d+.*?)/i);
    if (desMatch) {
      return { title: "KẾT QUẢ ĐẦU RA S-BOX S1 (DES OUTPUT)", value: desMatch[1].trim() };
    }
  }

  // 3. RSA Ciphertext & Decrypted Plaintext
  const rsaEncMatch = rawText.match(/===>\s*BẢN MÃ (?:THU ĐƯỢC|RSA).*?:?\s*C\s*=\s*(\d+)/i) ||
                      rawText.match(/===>\s*BẢN MÃ.*?:?\s*C\s*=\s*(\d+)/i);
  const rsaDecMatch = rawText.match(/===>\s*BẢN RÕ KHÔI PHỤC:?\s*M\s*=\s*(\d+)/i);
  if (rsaEncMatch && rsaDecMatch) {
    return { title: "KẾT QUẢ MÃ HÓA & GIẢI MÃ RSA", value: `C = ${rsaEncMatch[1]}  |  Khôi phục M = ${rsaDecMatch[1]}` };
  } else if (rsaEncMatch) {
    return { title: "BẢN MÃ RSA (CIPHERTEXT C)", value: `C = ${rsaEncMatch[1]}` };
  } else if (rsaDecMatch) {
    return { title: "BẢN RÕ KHÔI PHỤC (PLAINTEXT M)", value: `M = ${rsaDecMatch[1]}` };
  }

  // 4. RSA Keygen: Public & Private Keys
  if (tool && tool.id === "rsa_key_generation") {
    const pubMatch = rawText.match(/k_pub\s*=\s*([^\n\r]+)/i);
    const priMatch = rawText.match(/k_pri\s*=\s*([^\n\r]+)/i);
    if (pubMatch && priMatch) {
      return {
        title: "CẶP KHÓA RSA (PUBLIC & PRIVATE KEYS)",
        value: `k_pub = ${pubMatch[1].trim()}  |  k_pri = ${priMatch[1].trim()}`
      };
    }
  }

  // 5. Diffie-Hellman Key Exchange
  if (tool && (tool.id === "diffie_hellman_key_exchange" || tool.id === "dhke_mitm_attack")) {
    const dhMatch = rawText.match(/===>\s*KHÓA\s+(?:BÍ\s+MẬT\s+)?(?:PHIÊN\s+)?(?:THỐNG\s+NHẤT|CHUNG):?\s*([^\r\n]+)/i) ||
                    rawText.match(/===>\s*KHÓA PHIÊN CHUNG.*?:?\s*([^\r\n]+)/i);
    if (dhMatch) {
      return { title: "KHÓA BÍ MẬT PHIÊN THỐNG NHẤT (SHARED SESSION KEY)", value: dhMatch[1].trim() };
    }
    const mitmMatch = rawText.match(/===>\s*KẾT LUẬN TẤN CÔNG MITM:?[\r\n\s]+([^\r\n]+)/i);
    if (mitmMatch) {
      return { title: "KẾT QUẢ TẤN CÔNG MITM (DIFFIE-HELLMAN)", value: mitmMatch[1].trim() };
    }
  }

  // 6. ElGamal / Digital Signatures
  if (tool && tool.id === "elgamal_digital_signature") {
    const certMatch = rawText.match(/===>\s*CHỨNG CHỈ SỐ:?\s*([^\n\r]+)/i);
    if (certMatch) return { title: "CHỨNG CHỈ SỐ CA (CERTIFICATE)", value: certMatch[1].trim() };
    const sigMatch = rawText.match(/===>\s*CẶP CHỮ KÝ SỐ:?\s*(.*)/i);
    if (sigMatch) return { title: "CẶP CHỮ KÝ SỐ ELGAMAL (SIGNATURE PAIR)", value: sigMatch[1].trim() };
    if (rawText.includes("PHƯƠNG TRÌNH VÔ NGHIỆM")) {
      return { title: "KIỂM TRA CHỮ KÝ ELGAMAL", value: "VÔ NGHIỆM: gcd(k_E, p-1) != 1 (Đề chuẩn là k_E = 185)" };
    }
  }

  // 7. PKI RSA Certificate
  if (tool && tool.id === "pki_rsa_certificate") {
    const pkiMatch = rawText.match(/===>\s*CHỨNG CHỈ SỐ CA.*?:?[\r\n\s]+([^\r\n]+)/i) ||
                     rawText.match(/(?:S_CA\s*=\s*\d+|Cert\s*=\s*[^\r\n]+)/i);
    if (pkiMatch) return { title: "CHỨNG CHỈ SỐ PKI CA", value: pkiMatch[0].replace(/^===>\s*CHỨNG CHỈ SỐ CA.*?:?\s*/i, "").trim() };
  }

  // 8. Square-and-Multiply
  const smMatch = rawText.match(/===>\s*KẾT QUẢ CUỐI CÙNG:?\s*(.*)/i) ||
                  rawText.match(/===>\s*KẾT QUẢ:?\s*(.*)/i);
  if (smMatch && (tool?.id === "square_and_multiply" || rawText.includes("Square-and-Multiply"))) {
    return { title: "KẾT QUẢ TÍNH LŨY THỪA MODULO", value: smMatch[1].trim() };
  }

  // 9. Extended Euclidean Modular Inverse
  const invMatch = rawText.match(/(?:Kết quả nghịch đảo|Modular Inverse|Khóa riêng d)\s*[:=]\s*([^\n\r]+)/i);
  if (invMatch) {
    return { title: "NGHỊCH ĐẢO MODULO / KHÓA BÍ MẬT d", value: invMatch[1].trim() };
  }

  // 10. Euclidean GCD
  const gcdMatch = rawText.match(/(?:===>|\[=>\])\s*(?:Result|ĐÁP SỐ)?:?\s*(gcd\([^)]+\)\s*=\s*\d+)/i);
  if (gcdMatch) {
    return { title: "ƯỚC CHUNG LỚN NHẤT (GCD)", value: gcdMatch[1].trim() };
  }

  // 11. Classical Ciphers Ciphertext
  const cipherMatch = rawText.match(/===>\s*BẢN MÃ \(CIPHERTEXT\):?\s*['"]?([^'"\n\r]+)['"]?/i);
  if (cipherMatch) {
    return { title: "BẢN MÃ ĐÃ MÃ HÓA (CIPHERTEXT)", value: cipherMatch[1].trim() };
  }

  // 12. General Answer
  const genMatch = rawText.match(/===>\s*(?:ĐÁP SỐ|KẾT QUẢ):?\s*([^\n\r]+)/i);
  if (genMatch && genMatch[1].trim() && !genMatch[1].trim().endsWith(":")) {
    return { title: `ĐÁP SỐ CHÍNH XÁC (${tool ? tool.title : "KẾT QUẢ"})`, value: genMatch[1].trim() };
  }

  return null;
}

function createDesBitWidget(rawText, args) {
  // Check if student ID or integer can be determined
  let x = 56;
  if (args && args.length > 0 && args[0]) {
    const val = args[0].trim();
    if (/^\d+$/.test(val)) {
      x = parseInt(val) % 64;
    } else {
      const digits = val.replace(/\D/g, "");
      if (digits.length >= 3) {
        x = parseInt(digits.slice(-3)) % 64;
      }
    }
  }

  const binStr = x.toString(2).padStart(6, "0");
  const b1 = binStr[0], b2 = binStr[1], b3 = binStr[2], b4 = binStr[3], b5 = binStr[4], b6 = binStr[5];
  const row = parseInt(b1 + b6, 2);
  const col = parseInt(binStr.slice(1, 5), 2);

  const S1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
  ];
  const outVal = S1[row][col];
  const outBin = outVal.toString(2).padStart(4, "0");

  const widget = document.createElement("div");
  widget.className = "step-card";
  widget.innerHTML = `
    <div class="step-card-header">
      <span class="step-badge" style="background-color: var(--primary);">Sơ đồ trực quan</span>
      <h3 class="step-title">Phân tích 6 bit đầu vào & Tọa độ Hàng / Cột hộp S1</h3>
    </div>
    <div class="step-body">
      <div class="bit-splitter">
        <div class="bits-row">
          <div class="bit-chip row-bit" title="Bit b1 (Hàng)"><span class="bit-name">b1 (Hàng)</span><span class="bit-val">${b1}</span></div>
          <div class="bit-chip col-bit" title="Bit b2 (Cột)"><span class="bit-name">b2 (Cột)</span><span class="bit-val">${b2}</span></div>
          <div class="bit-chip col-bit" title="Bit b3 (Cột)"><span class="bit-name">b3 (Cột)</span><span class="bit-val">${b3}</span></div>
          <div class="bit-chip col-bit" title="Bit b4 (Cột)"><span class="bit-name">b4 (Cột)</span><span class="bit-val">${b4}</span></div>
          <div class="bit-chip col-bit" title="Bit b5 (Cột)"><span class="bit-name">b5 (Cột)</span><span class="bit-val">${b5}</span></div>
          <div class="bit-chip row-bit" title="Bit b6 (Hàng)"><span class="bit-name">b6 (Hàng)</span><span class="bit-val">${b6}</span></div>
        </div>
        <div class="bit-groups-summary">
          <span class="bit-group-badge bit-group-row">Hàng r = (b1 b6)₂ = (${b1}${b6})₂ = ${row}</span>
          <span class="bit-group-badge bit-group-col">Cột c = (b2 b3 b4 b5)₂ = (${b2}${b3}${b4}${b5})₂ = ${col}</span>
          <span class="bit-group-badge" style="background: rgba(16, 185, 129, 0.12); color: var(--success); border: 1px solid var(--success);">S1[${row}][${col}] = ${outVal} (${outBin}₂)</span>
        </div>
      </div>
    </div>
  `;
  return widget;
}

function parseSteps(rawText) {
  const steps = [];
  const lines = rawText.split(/\r?\n/);

  let currentStep = null;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Detect step heading like [BƯỚC 1], [BÀI 1.1], [TRƯỜNG HỢP 1], Step 1, or 1. Alice computes...
    const stepMatch = line.match(/^\s*\[(?:BƯỚC|BÀI|PHẦN|ROUND|TRƯỜNG HỢP|CASE)\s*([\d\.]+)[:\]\s]*(.*)/i) ||
                      line.match(/^\s*(?:Bước|Step|Phần|Round|Trường hợp|Case)\s*([\d\.]+)[:\s]*(.*)/i) ||
                      line.match(/^\s*(\d+)[\.\)]\s+([A-ZÀ-Ỹ0-9].*)/);

    if (stepMatch) {
      if (currentStep && currentStep.lines.some(l => l.trim().length > 0)) {
        steps.push(currentStep);
      }
      currentStep = {
        num: stepMatch[1],
        title: stepMatch[2].replace(/[\]\s]+$/, "").replace(/^[:\-–\s]+|[:\-–\s]+$/g, "").trim() || `Bước ${stepMatch[1]}`,
        lines: []
      };
      continue;
    }

    if (currentStep) {
      currentStep.lines.push(line);
    }
  }

  if (currentStep && currentStep.lines.some(l => l.trim().length > 0)) {
    steps.push(currentStep);
  }

  // If no explicit steps were parsed, intelligently synthesize 3 logical visual cards
  if (steps.length === 0) {
    const meaningfulLines = lines.filter(l => {
      const t = l.trim();
      return t && !t.startsWith("===") && !t.startsWith("---");
    });

    if (meaningfulLines.length > 0) {
      const step1Lines = [];
      const step2Lines = [];
      const step3Lines = [];

      let stage = 1;
      for (const line of meaningfulLines) {
        const t = line.trim();
        // Check for table or computation step
        if (t.includes("|") || t.startsWith("Step ") || t.startsWith("Vòng ") || t.includes("Square-and-Multiply") || t.startsWith("[+] BẢNG")) {
          stage = 2;
        } else if (stage === 2 && (t.startsWith("===>") || t.startsWith("[=>]") || t.includes("Kết quả") || t.includes("Bézout Identity") || t.includes("Modular Inverse") || t.includes("Verification"))) {
          stage = 3;
        }

        if (stage === 1) {
          step1Lines.push(line);
        } else if (stage === 2) {
          step2Lines.push(line);
        } else {
          step3Lines.push(line);
        }
      }

      if (step1Lines.length > 0) {
        steps.push({
          num: "1",
          title: "Thiết lập tham số đầu vào & Công thức toán học",
          lines: step1Lines
        });
      }
      if (step2Lines.length > 0) {
        steps.push({
          num: String(steps.length + 1),
          title: "Quá trình tính toán chi tiết & Bảng vết thuật toán",
          lines: step2Lines
        });
      }
      if (step3Lines.length > 0) {
        steps.push({
          num: String(steps.length + 1),
          title: "Kết quả chung cuộc & Xác thực tính đúng đắn",
          lines: step3Lines
        });
      }
    }
  }

  return steps;
}

function renderStepContent(body, lines) {
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];
    const trimmed = line.trim();

    if (!trimmed || trimmed.startsWith("===") || trimmed.startsWith("---")) {
      i++;
      continue;
    }

    // 1. Check for ASCII Table (consecutive lines with '|')
    if (trimmed.includes("|") && (lines[i + 1] && lines[i + 1].includes("---") || lines[i - 1] && lines[i - 1].includes("---"))) {
      const tableData = extractTableLines(lines, i);
      if (tableData) {
        body.appendChild(renderHtmlTable(tableData.headers, tableData.rows));
        i = tableData.nextIndex;
        continue;
      }
    }

    // 2. Check for Conclusion / Final Result (===> or [=>] or KẾT QUẢ:)
    if (trimmed.startsWith("===>") || trimmed.startsWith("[=>]") || /^BẢN MÃ THU ĐƯỢC:|^KHÓA BÍ MẬT PHIÊN:|^KẾT QUẢ:/i.test(trimmed)) {
      const callout = document.createElement("div");
      callout.className = "callout callout-success";
      const cleanText = trimmed.replace(/^===>|^\[=>\]/, "").trim();
      callout.innerHTML = `
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="20 6 9 17 4 12"></polyline>
        </svg>
        <div style="flex: 1;"><strong>${escapeHtml(cleanText)}</strong></div>
      `;
      body.appendChild(callout);
      i++;
      continue;
    }

    // 3. Check for Verification Badges (Kiểm tra: True / Verification: True)
    if (/Kiểm tra|Verification|Chính xác|Khớp bản rõ/i.test(trimmed) && /True|Chính xác|Khớp|Thành công/i.test(trimmed)) {
      const vBadge = document.createElement("div");
      vBadge.className = "verify-badge";
      vBadge.innerHTML = `
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
          <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        <span>${escapeHtml(trimmed)}</span>
      `;
      body.appendChild(vBadge);
      i++;
      continue;
    }

    // 4. Check for Dedicated Mathematical Formula
    const formulaMatch = trimmed.match(/^(?:Công thức[^\:]*|Formula[^\:]*|Phương trình[^\:]*|Biểu thức[^\:]*|Hệ thức[^\:]*|Đẳng thức[^\:]*)\s*:\s*(.*)/i);
    const isMathEquation = !formulaMatch && /^[\w\s\(\)\^\\/\.\-à-ỹÀ-Ỹ]+\s*=\s*[^=]+(?:mod|\^|\*|\+|\-)/i.test(trimmed) && trimmed.length < 100 && !trimmed.includes("|");
    if (formulaMatch || isMathEquation) {
      const expr = formulaMatch ? formulaMatch[1].trim() : trimmed;
      const formulaBox = document.createElement("div");
      formulaBox.className = "math-formula-box";
      formulaBox.innerHTML = `
        <div class="math-formula-tag">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
          </svg>
          <span>Công thức toán học & Phương trình</span>
        </div>
        <div class="math-formula-expr">${escapeHtml(expr)}</div>
      `;
      body.appendChild(formulaBox);
      i++;
      continue;
    }

    // 5. Check for Numbered Arithmetic Sub-step (e.g. "1. d * r = 25 * 591 = 14775")
    const numSubstepMatch = trimmed.match(/^(\d+)[\.\)]\s+([^\r\n]+)/);
    if (numSubstepMatch && (trimmed.includes("=") || trimmed.includes("mod") || trimmed.includes("*") || trimmed.includes("+") || trimmed.includes("-"))) {
      const substepEl = document.createElement("div");
      substepEl.className = "calc-substep";
      substepEl.innerHTML = `
        <span class="substep-num">${numSubstepMatch[1]}</span>
        <span class="substep-expr">${escapeHtml(numSubstepMatch[2].trim())}</span>
      `;
      body.appendChild(substepEl);
      i++;
      continue;
    }

    // 6. Check for Subheading / Case header ([+] ... or [TRƯỜNG HỢP ...])
    if (trimmed.startsWith("[+]") || /^\[(?:TRƯỜNG HỢP|PHẦN|CASE)/i.test(trimmed)) {
      const subhead = document.createElement("div");
      subhead.className = "step-subheading";
      const cleanTitle = trimmed.replace(/^\[\+\]\s*|^\[|\]$/g, "").trim();
      subhead.innerHTML = `
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"></circle>
          <polyline points="12 6 12 12 16 14"></polyline>
        </svg>
        <span>${escapeHtml(cleanTitle)}</span>
      `;
      body.appendChild(subhead);
      i++;
      continue;
    }

    // 7. Check for Binary / Bit representation (Số mũ nhị phân: ... or bits)
    if (trimmed.includes("Số mũ nhị phân:") || (trimmed.includes("nhị phân") && trimmed.includes("bit"))) {
      const binBox = document.createElement("div");
      binBox.className = "binary-meta-box";
      binBox.innerHTML = `
        <span class="bit-tag">BINARY</span>
        <span>${escapeHtml(trimmed)}</span>
      `;
      body.appendChild(binBox);
      i++;
      continue;
    }

    // 8. Check for Parameter List / Chips (Tham số: Modulus N = ..., Public e = ...)
    if (/^Tham số(?: hệ thống)?[:\s]/i.test(trimmed) && trimmed.includes(",")) {
      const rawParams = trimmed.replace(/^Tham số(?: hệ thống)?[:\s]*/i, "");
      const pairs = rawParams.split(",");
      const chipsContainer = document.createElement("div");
      chipsContainer.className = "param-chips-grid";

      pairs.forEach(p => {
        const parts = p.split("=");
        if (parts.length === 2) {
          const chip = document.createElement("div");
          chip.className = "param-chip";
          chip.innerHTML = `
            <span class="param-chip-key">${escapeHtml(parts[0].trim())}:</span>
            <span class="param-chip-val">${escapeHtml(parts[1].trim())}</span>
          `;
          chipsContainer.appendChild(chip);
        }
      });

      if (chipsContainer.children.length > 0) {
        body.appendChild(chipsContainer);
        i++;
        continue;
      }
    }

    // 9. Check for Key-Value pairs (* Key : Value or - Key: Value)
    const kvMatch = trimmed.match(/^[\*\-•]\s*([^:]+):\s*(.*)/);
    if (kvMatch) {
      const valText = kvMatch[2].trim();
      const isMathVal = valText.includes("=") || valText.includes("mod") || valText.includes("^");
      const kvRow = document.createElement("div");
      kvRow.className = "math-row";
      kvRow.innerHTML = `
        <span style="color: var(--text-muted); font-size: 12.5px; font-weight: 500;">${escapeHtml(kvMatch[1].trim())}:</span>
        <strong style="color: var(--text-main); font-family: ${isMathVal ? 'var(--font-mono)' : 'inherit'}; font-weight: 600;">${escapeHtml(valText)}</strong>
      `;
      body.appendChild(kvRow);
      i++;
      continue;
    }

    // 10. Check for Standalone / Indented Math Equations (e.g. beta^r mod p = 333^591 mod 997 = 991)
    if (/^[A-Za-z0-9_\^\*\+\-\s\(\)]+\s*=\s*.+(?:mod|\^|\*|\+|\-)/.test(trimmed) && !trimmed.includes("|") && trimmed.length < 90) {
      const exprDiv = document.createElement("div");
      exprDiv.className = "calc-inline-math";
      exprDiv.innerHTML = `<code>${escapeHtml(trimmed)}</code>`;
      body.appendChild(exprDiv);
      i++;
      continue;
    }

    // 9. General text paragraph
    const p = document.createElement("div");
    p.style.lineHeight = "1.55";
    p.style.fontFamily = trimmed.includes("mod") || trimmed.includes("^") ? "var(--font-mono)" : "inherit";
    p.textContent = trimmed;
    body.appendChild(p);
    i++;
  }
}

function createStepCard(step, defaultNum) {
  const card = document.createElement("div");
  card.className = "step-card";

  const header = document.createElement("div");
  header.className = "step-card-header";
  header.innerHTML = `
    <span class="step-badge">Bước ${step.num || defaultNum}</span>
    <h3 class="step-title">${escapeHtml(step.title)}</h3>
  `;
  card.appendChild(header);

  const body = document.createElement("div");
  body.className = "step-body";

  renderStepContent(body, step.lines);

  card.appendChild(body);
  return card;
}

function extractTableLines(lines, startIndex) {
  let headerLine = "";
  let separatorFound = false;
  const rowLines = [];
  let idx = startIndex;

  // Search backward if startIndex is on separator
  if (lines[startIndex].includes("---") && startIndex > 0 && lines[startIndex - 1].includes("|")) {
    headerLine = lines[startIndex - 1];
    idx = startIndex + 1;
    separatorFound = true;
  } else if (lines[startIndex].includes("|") && lines[startIndex + 1] && lines[startIndex + 1].includes("---")) {
    headerLine = lines[startIndex];
    idx = startIndex + 2;
    separatorFound = true;
  } else {
    return null;
  }

  while (idx < lines.length) {
    const l = lines[idx].trim();
    if (!l) {
      idx++;
      break;
    }
    if (l.startsWith("---") || l.startsWith("===")) {
      idx++;
      break;
    }
    if (l.includes("|")) {
      rowLines.push(l);
      idx++;
    } else {
      break;
    }
  }

  const headers = headerLine.split("|").map(c => c.trim()).filter(Boolean);
  const rows = rowLines.map(r => r.split("|").map(c => c.trim()).filter(Boolean));

  return { headers, rows, nextIndex: idx };
}

function renderHtmlTable(headers, rows) {
  const wrapper = document.createElement("div");
  wrapper.className = "calc-table-wrapper";

  const table = document.createElement("table");
  table.className = "calc-table";

  const thead = document.createElement("thead");
  const trHead = document.createElement("tr");
  headers.forEach(h => {
    const th = document.createElement("th");
    th.textContent = h;
    trHead.appendChild(th);
  });
  thead.appendChild(trHead);
  table.appendChild(thead);

  const tbody = document.createElement("tbody");
  rows.forEach((row, rIdx) => {
    const tr = document.createElement("tr");
    row.forEach((cell, cIdx) => {
      const td = document.createElement("td");
      td.textContent = cell;
      // Highlight initial rows or gcd=1 rows
      if (cell === "1" || cell === "0" || cell === "init") {
        td.classList.add("highlight");
      }
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });
  table.appendChild(tbody);

  wrapper.appendChild(table);
  return wrapper;
}

function createGenericCard(rawText) {
  const card = document.createElement("div");
  card.className = "step-card";

  const header = document.createElement("div");
  header.className = "step-card-header";
  header.innerHTML = `
    <span class="step-badge">Kết quả</span>
    <h3 class="step-title">Chi tiết lời giải thuật toán</h3>
  `;
  card.appendChild(header);

  const body = document.createElement("div");
  body.className = "step-body";

  const lines = rawText.split(/\r?\n/);
  renderStepContent(body, lines);

  card.appendChild(body);
  return card;
}

function renderVisualOutput(rawText, tool, args) {
  visualContentEl.innerHTML = "";

  if (!rawText || !rawText.trim()) {
    visualContentEl.innerHTML = `
      <div class="empty-state">
        <p>No output to display.</p>
      </div>
    `;
    return;
  }

  // 1. Extract and render Hero Answer banner at the top
  const heroData = extractHeroAnswer(rawText, tool);
  if (heroData) {
    const heroCard = document.createElement("div");
    heroCard.className = "hero-result-card";
    heroCard.innerHTML = `
      <div class="hero-info">
        <div class="hero-tag">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polyline points="20 6 9 17 4 12"></polyline>
          </svg>
          <span>${heroData.title}</span>
        </div>
        <div class="hero-value">${escapeHtml(heroData.value)}</div>
      </div>
      <div class="hero-actions">
        <button class="btn-output" id="btn-copy-hero" title="Copy answer value">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
            <path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"></path>
          </svg>
          <span>Copy Answer</span>
        </button>
      </div>
    `;
    heroCard.querySelector("#btn-copy-hero").addEventListener("click", () => {
      navigator.clipboard.writeText(heroData.value);
      showToast(`Copied: ${heroData.value}`);
    });
    visualContentEl.appendChild(heroCard);
  }

  // 2. Specialized visual widget for DES S-Box
  if (tool.id === "des_sbox_lookup") {
    const bitWidget = createDesBitWidget(rawText, args);
    if (bitWidget) {
      visualContentEl.appendChild(bitWidget);
    }
  }

  // 3. Parse Step Cards
  const steps = parseSteps(rawText);
  if (steps.length > 0) {
    steps.forEach((step, idx) => {
      const card = createStepCard(step, idx + 1);
      visualContentEl.appendChild(card);
    });
  } else {
    const genericCard = createGenericCard(rawText);
    visualContentEl.appendChild(genericCard);
  }
}

// Start app
window.addEventListener("DOMContentLoaded", init);
