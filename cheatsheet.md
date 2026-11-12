<style>
@page {
  size: A4 portrait;
  margin: 2.2mm 3.2mm 2.2mm 3.2mm;
}
@media print {
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    font-size: 5.7pt;
    line-height: 1.11;
    color: #000;
    background: #fff;
    margin: 0;
    padding: 0;
  }
  h1 { 
    font-size: 7.8pt; 
    margin: 0 0 1px 0; 
    text-align: center; 
    font-weight: 800; 
    color: #1e3a8a; 
    text-transform: uppercase; 
    border-bottom: 0.8px solid #1e3a8a; 
    padding-bottom: 0.5px; 
  }
  .meta-sub {
    font-size: 5.2pt;
    text-align: center;
    color: #475569;
    font-weight: 700;
    margin-bottom: 1px;
  }
  .grid-3col { 
    display: grid; 
    grid-template-columns: 1fr 1fr 1fr; 
    column-gap: 2mm; 
    row-gap: 0.8mm; 
  }
  .box { 
    border: 0.6px solid #475569; 
    border-radius: 1.5px; 
    padding: 1px 1.8mm; 
    background: #fff; 
    break-inside: avoid;
    margin-bottom: 0.8mm;
  }
  .box-title { 
    font-size: 6.0pt; 
    font-weight: 800; 
    color: #0f172a; 
    background: #f1f5f9; 
    margin: -1px -1.8mm 1px -1.8mm; 
    padding: 0.6px 1.8mm; 
    border-bottom: 0.5px solid #94a3b8; 
    text-transform: uppercase;
  }
  .f { 
    font-family: "Courier New", Consolas, monospace; 
    font-weight: 700; 
    color: #1d4ed8; 
    font-size: 5.8pt; 
  }
  .st { font-weight: 800; color: #047857; }
  .kw { font-weight: 800; color: #b91c1c; }
  .cho { font-weight: 800; color: #b45309; }
  .tinh { font-weight: 800; color: #6d28d9; }
  table.eea { 
    width: 100%; 
    border-collapse: collapse; 
    font-size: 5.3pt; 
    margin: 0.6px 0; 
  }
  table.eea th, table.eea td { 
    border: 0.4px solid #64748b; 
    padding: 0.2px 0.5px; 
    text-align: center; 
  }
  table.eea th { 
    background: #f8fafc; 
    font-weight: 700; 
  }
  ul { margin: 0; padding-left: 7.5px; }
  li { margin-bottom: 0.3px; }
  p { margin: 0.3px 0; }
}
@media screen {
  body { font-family: sans-serif; font-size: 11px; line-height: 1.35; padding: 12px; max-width: 1350px; margin: 0 auto; }
  .grid-3col { display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 10px; }
  .box { border: 1px solid #cbd5e1; border-radius: 4px; padding: 6px; margin-bottom: 8px; }
  .box-title { font-weight: bold; background: #f1f5f9; padding: 3px 5px; margin: -6px -6px 5px -6px; }
  table.eea { width: 100%; border-collapse: collapse; margin: 4px 0; font-size: 9.5px; }
  table.eea th, table.eea td { border: 1px solid #cbd5e1; padding: 2px 4px; text-align: center; }
  .f { font-family: monospace; font-weight: bold; color: #1d4ed8; }
  .st { font-weight: bold; color: #047857; }
  .kw { font-weight: bold; color: #b91c1c; }
  .cho { font-weight: bold; color: #b45309; }
  .tinh { font-weight: bold; color: #6d28d9; }
}
</style>

# USTH CRYPTOGRAPHY - FORMULAS & STEP-BY-STEP PROBLEM SOLVING GUIDE (A4)
<div class="meta-sub">Exam Room Cheatsheet | Standard Step-by-Step Template for Writing Solutions | General Formulas | Compute via Tool</div>

<div class="grid-3col">

<!-- ==================== COLUMN 1: ARITHMETIC FOUNDATIONS & CLASSICAL ==================== -->
<div class="col">

  <!-- FORM 1: DES S-BOX -->
  <div class="box">
    <div class="box-title">FORM 1: DES S-BOX S1 LOOKUP (3 POINTS)</div>
    <p><span class="cho">GIVEN:</span> Student ID (or decimal integer $x_{raw}$), S-Box $S_1$ matrix ($4 \text{ rows} \times 16 \text{ cols}$).</p>
    <p><span class="tinh">FIND:</span> 4-bit output $(y_1 y_2 y_3 y_4)_2$ and decimal value $\text{Val}$.</p>
    <p><span class="st">STEPS:</span></p>
    <ul>
      <li><span class="st">Step 1:</span> Reduce: <span class="f">$x = (\text{Student\_ID}) \pmod{64}$</span> ($0 \le x < 64$).</li>
      <li><span class="st">Step 2:</span> Convert $x \to$ 6-bit binary: <span class="f">$x = (b_1 b_2 b_3 b_4 b_5 b_6)_2$</span>.</li>
      <li><span class="st">Step 3:</span> Row & Column indices:
        <br>• <b>Row $r$:</b> Outer bits: <span class="f">$r = (b_1 b_6)_2 \in \{0, 1, 2, 3\}$</span>.
        <br>• <b>Column $c$:</b> Middle 4 bits: <span class="f">$c = (b_2 b_3 b_4 b_5)_2 \in \{0 \dots 15\}$</span>.
      </li>
      <li><span class="st">Step 4:</span> Lookup matrix: <span class="f">$\text{Val} = S_1[r][c]$</span> (in decimal).
        <br><i>Note:</i> Odd ID $\to$ choose Set 1; Even ID $\to$ choose Set 2 (2023 exam).
      </li>
      <li><span class="st">Step 5:</span> Convert $\text{Val} \to$ 4-bit binary: <span class="f">$(y_1 y_2 y_3 y_4)_2$</span>.</li>
    </ul>
  </div>

  <!-- FORM 2: EEA TABLE -->
  <div class="box">
    <div class="box-title">FORM 2: EXTENDED EUCLIDEAN ALGORITHM (EEA) INVERSE</div>
    <p><span class="cho">GIVEN:</span> Integer $e$ (or $a$) and modulus $m$ with $\gcd(e, m) = 1$.</p>
    <p><span class="tinh">FIND:</span> Modular inverse <span class="f">$d = e^{-1} \pmod m$</span> such that <span class="f">$e \cdot d \equiv 1 \pmod m$</span>.</p>
    <p><span class="st">STEPS:</span></p>
    <ul>
      <li><span class="st">Step 1:</span> Draw a 6-column table: <code>Step | q | r | s | t | Division Equation</code>.</li>
      <li><span class="st">Step 2:</span> 2 Initialization rows:
        <br>• Row 0: $r_0 = m$, $s_0 = 1$, $t_0 = 0$. (Eq: $r_0 = m$).
        <br>• Row 1: $r_1 = e$, $s_1 = 0$, $t_1 = 1$. (Eq: $r_1 = e$).
      </li>
      <li><span class="st">Step 3:</span> Compute each row $i \ge 2$ using recurrence relations:
        <table class="eea">
          <tr><th>q</th><th>r</th><th>s</th><th>t</th><th>Division Equation</th></tr>
          <tr><td>$q_i = \lfloor r_{i-2} / r_{i-1} \rfloor$</td><td>$r_i = r_{i-2} - q_i r_{i-1}$</td><td>$s_i = s_{i-2} - q_i s_{i-1}$</td><td>$t_i = t_{i-2} - q_i t_{i-1}$</td><td>$r_{i-2} = q_i \cdot r_{i-1} + r_i$</td></tr>
        </table>
      </li>
      <li><span class="st">Step 4:</span> Stop when $r_i = 0$. Preceding row gives $\gcd(e, m) = r_{i-1} = 1$.</li>
      <li><span class="st">Step 5:</span> Extract <span class="f">$d \equiv t_{i-1} \pmod m$</span>. If $t_{i-1} < 0 \implies \mathbf{d = t_{i-1} + m}$.</li>
    </ul>
  </div>

  <!-- FORM 3: SQUARE-AND-MULTIPLY -->
  <div class="box">
    <div class="box-title">FORM 3: FAST EXPONENTIATION (SQUARE-AND-MULTIPLY)</div>
    <p><span class="cho">GIVEN:</span> Base $x$, large exponent $c$, modulus $n$.</p>
    <p><span class="tinh">FIND:</span> Modular exponentiation value <span class="f">$y = x^c \pmod n$</span>.</p>
    <p><span class="st">STEPS:</span></p>
    <ul>
      <li><span class="st">Step 1:</span> Convert exponent to binary: <span class="f">$c = (b_k b_{k-1} \dots b_1 b_0)_2$</span>.</li>
      <li><span class="st">Step 2:</span> Draw 5-column table: <code>Step | Bit b_i | Operation | Calculation | Value y</code>.</li>
      <li><span class="st">Step 3:</span> Initialize $y = 1$. Scan from MSB $b_k$ down to LSB $b_0$:
        <br>• <b>Every bit:</b> Always compute <span class="f">Square: $y = y^2 \pmod n$</span>.
        <br>• <b>If bit $b_i = 1$:</b> Additionally compute <span class="f">Multiply: $y = (y \cdot x) \pmod n$</span>.
      </li>
      <li><span class="st">Step 4:</span> The value $y$ in the final row is the exact result.</li>
    </ul>
  </div>

  <!-- FORM 4: CLASSICAL CIPHERS & CRT -->
  <div class="box">
    <div class="box-title">FORM 4: CLASSICAL CIPHERS & CHINESE REMAINDER (CRT)</div>
    <p><b>A. Classical Ciphers (Given plaintext $P$, key $K \implies$ Encrypt $C$ & Decrypt $P$):</b></p>
    <ul>
      <li><b>Caesar:</b> Encrypt $C = (P + k) \pmod{26}$ | Decrypt $P = (C - k) \pmod{26}$.</li>
      <li><b>Affine:</b> $C = (aP + b) \pmod{26}$ ($\gcd(a, 26) = 1$).
        <br>Decrypt: <span class="f">$P = a^{-1}(C - b) \pmod{26}$</span> (find $a^{-1} \pmod{26}$ via EEA).
      </li>
      <li><b>Vigenère:</b> Repeat key $K$: $C_i = (P_i + K_i) \pmod{26}$ | $P_i = (C_i - K_i) \pmod{26}$.</li>
      <li><b>OTP / Vernam:</b> $C = P \oplus K$ | $P = C \oplus K$ (Perfect Secrecy).</li>
    </ul>
    <p><b>B. Chinese Remainder Theorem (CRT):</b></p>
    <p><span class="cho">GIVEN:</span> System $x \equiv a_i \pmod{m_i}$ with pairwise coprime $\gcd(m_i, m_j) = 1$.</p>
    <p><span class="tinh">FIND:</span> Unique simultaneous solution <span class="f">$x \pmod M$</span>.</p>
    <ul>
      <li><span class="st">Step 1:</span> Compute product $M = \prod m_i = m_1 \cdot m_2 \cdots m_k$.</li>
      <li><span class="st">Step 2:</span> Compute $M_i = M/m_i$ and modular inverse $y_i = M_i^{-1} \pmod{m_i}$ (EEA).</li>
      <li><span class="st">Step 3:</span> Unique solution: <span class="f">$x = \left(\sum a_i M_i y_i\right) \pmod M$</span>.</li>
    </ul>
  </div>

</div>

<!-- ==================== COLUMN 2: RSA, PKI CERTIFICATES, BLOCK CIPHERS ==================== -->
<div class="col">

  <!-- FORM 5: RSA KEY GENERATION -->
  <div class="box">
    <div class="box-title">FORM 5: RSA KEY GENERATION</div>
    <p><span class="cho">GIVEN:</span> Two prime numbers $p, q$ (or given $N, p \implies q = N/p$).</p>
    <p><span class="tinh">FIND:</span> Public Key <span class="f">$k_{pub} = (N, e)$</span> and Private Key <span class="f">$k_{pri} = (N, d)$</span>.</p>
    <p><span class="st">STEPS:</span></p>
    <ul>
      <li><span class="st">Step 1:</span> Compute Modulus: <span class="f">$N = p \cdot q$</span>.</li>
      <li><span class="st">Step 2:</span> Compute Euler totient: <span class="f">$\Phi(N) = (p - 1)(q - 1)$</span>.</li>
      <li><span class="st">Step 3:</span> Choose public exponent $e$:
        <br>• Condition: $1 < e < \Phi(N)$ and <span class="kw">$\gcd(e, \Phi(N)) = 1$</span>.
        <br>• Factorize $\Phi(N)$ to prove $e$ is coprime.
      </li>
      <li><span class="st">Step 4:</span> Compute private exponent $d$ via EEA (Form 2):
        <br><span class="f">$d = e^{-1} \pmod{\Phi(N)} \iff e \cdot d \equiv 1 \pmod{\Phi(N)}$</span>.
      </li>
      <li><span class="st">Step 5:</span> State keypairs:
        <br>• Public Key: <span class="f">$k_{pub} = (N, e)$</span> | Private Key: <span class="f">$k_{pri} = (N, d)$</span>.
      </li>
    </ul>
  </div>

  <!-- FORM 6: RSA ENCRYPT/DECRYPT -->
  <div class="box">
    <div class="box-title">FORM 6: RSA ENCRYPTION & DECRYPTION</div>
    <p><span class="cho">GIVEN:</span> Plaintext $M$ ($0 \le M < N$), public key $(N, e)$, private key $(N, d)$.</p>
    <p><span class="tinh">FIND:</span> Ciphertext $C$ and recovered plaintext $M_{dec}$.</p>
    <p><span class="st">STEPS:</span></p>
    <ul>
      <li><span class="st">Step 1 (Encrypt):</span> <span class="f">$C = M^e \pmod N$</span>.
        <br>Draw Square-and-Multiply table for $M^e \pmod N \implies$ Ciphertext $C$.
      </li>
      <li><span class="st">Step 2 (Decrypt):</span> <span class="f">$M = C^d \pmod N$</span>.
        <br>Draw Square-and-Multiply table for $C^d \pmod N \implies$ Plaintext $M$.
      </li>
      <li><span class="st">Step 3 (Verify & Proof):</span> Check <span class="kw">$M_{dec} == M$</span>.
        <br>Euler proof: $C^d \equiv (M^e)^d \equiv M^{k\Phi(N)+1} \equiv M \pmod N$.
      </li>
    </ul>
  </div>

  <!-- FORM 7: RSA CERTIFICATE & HYBRID EMAIL -->
  <div class="box">
    <div class="box-title">FORM 7: RSA CA CERTIFICATE & PKI HYBRID EMAIL</div>
    <p><b>A. RSA CA Digital Certificate:</b></p>
    <p><span class="cho">GIVEN:</span> User ID/key $M$, CA private key $d_{CA}$, CA public key $(N_{CA}, e_{CA})$.</p>
    <p><span class="tinh">FIND:</span> CA signature $S_{CA}$ and certificate verification.</p>
    <ul>
      <li><span class="st">CA Signing:</span> <span class="f">$S_{CA} = M^{d_{CA}} \pmod{N_{CA}}$</span>. Bundle $\text{Cert}_A = (M, S_{CA})$.</li>
      <li><span class="st">Verification:</span> Compute <span class="f">$V = (S_{CA})^{e_{CA}} \pmod{N_{CA}}$</span>. Check <span class="kw">$V == M$</span>.</li>
    </ul>
    <p><b>B. Secure PKI Hybrid Email Protocol:</b></p>
    <p><span class="cho">GIVEN:</span> Email $P$, Alice keypair $(e_A, d_A)$, Bob keypair $(e_B, d_B)$, $\text{Cert}_A$.</p>
    <p><span class="tinh">FIND:</span> Encrypted payload sent by Alice & Bob's decryption process.</p>
    <ul>
      <li><span class="st">Alice sends (5 steps):</span>
        <br>1. Generate random symmetric session key $K_{sym}$ (AES/DES).
        <br>2. Encrypt email: <span class="f">$C = E_{K_{sym}}(P)$</span>.
        <br>3. Encrypt session key: <span class="f">$C_K = K_{sym}^{e_B} \pmod{N_B}$</span>.
        <br>4. Sign message hash: <span class="f">$\sigma = (H(P))^{d_A} \pmod{N_A}$</span>.
        <br>5. Package & send to Bob: $\{C, C_K, \sigma, \text{Cert}_A\}$.
      </li>
      <li><span class="st">Bob receives (3 steps):</span>
        <br>1. Use $d_B$ to decrypt $C_K \implies$ recover key $K_{sym} = C_K^{d_B} \pmod{N_B}$.
        <br>2. Use $K_{sym}$ to decrypt $C \implies$ recover email body $P = D_{K_{sym}}(C)$.
        <br>3. Extract $e_A$ from $\text{Cert}_A$ and verify <span class="kw">$\sigma^{e_A} \pmod{N_A} == H(P)$</span>.
      </li>
    </ul>
  </div>

  <!-- FORM 8: BLOCK CIPHER MODES & FEISTEL -->
  <div class="box">
    <div class="box-title">FORM 8: BLOCK CIPHER MODES & FEISTEL NETWORK</div>
    <p><b>A. Block Cipher Modes of Operation:</b></p>
    <p><span class="cho">GIVEN:</span> Plaintext blocks $P_i$, symmetric key $K$, initialization vector IV.</p>
    <p><span class="tinh">FIND:</span> Ciphertext $C_i$ (or decrypted plaintext $P_i$):</p>
    <ul>
      <li><b>ECB:</b> $C_i = E_K(P_i)$ | $P_i = D_K(C_i)$. No IV $\implies$ leaks data patterns.</li>
      <li><b>CBC:</b> $C_0 = \text{IV}$; $C_i = E_K(P_i \oplus C_{i-1})$. Decrypt: <span class="f">$P_i = D_K(C_i) \oplus C_{i-1}$</span>.</li>
      <li><b>CFB:</b> $C_0 = \text{IV}$; $C_i = P_i \oplus E_K(C_{i-1})$. Decrypt: <span class="f">$P_i = C_i \oplus E_K(C_{i-1})$</span>.</li>
      <li><b>OFB:</b> $S_0 = \text{IV}$; $S_i = E_K(S_{i-1})$; $C_i = P_i \oplus S_i$. Decrypt: <span class="f">$P_i = C_i \oplus S_i$</span>.</li>
      <li><b>CTR:</b> $S_i = E_K(\text{IV} \mathbin{\Vert} i)$; $C_i = P_i \oplus S_i$. Enables parallel execution.</li>
    </ul>
    <p><b>B. Feistel Network (DES):</b></p>
    <p><span class="cho">GIVEN:</span> 64-bit block $(L_{i-1}, R_{i-1})$, round function $F$, subkey $K_i$.</p>
    <p><span class="tinh">FIND:</span> Round $i$ output $(L_i, R_i)$ and inverse decryption formulas:</p>
    <ul>
      <li>Round $i$ Encrypt: <span class="f">$L_i = R_{i-1}$</span> ; <span class="f">$R_i = L_{i-1} \oplus F(R_{i-1}, K_i)$</span>.</li>
      <li>Round $i$ Decrypt (reverse $K_{16} \to K_1$): <span class="f">$R_{i-1} = L_i$</span> ; <span class="f">$L_{i-1} = R_i \oplus F(L_i, K_i)$</span>.</li>
    </ul>
  </div>

</div>

<!-- ==================== COLUMN 3: ELGAMAL, DSA, DHKE, A5/1, SHA-1 ==================== -->
<div class="col">

  <!-- FORM 9: ELGAMAL DIGITAL SIGNATURE -->
  <div class="box">
    <div class="box-title">FORM 9: ELGAMAL DIGITAL SIGNATURE & CA CERTIFICATE</div>
    <p><span class="cho">GIVEN:</span> Prime $p$, generator $\alpha$, private key $d \implies \beta = \alpha^d \pmod p$, message $x$ (or $x_A = x + e_A$), ephemeral key $k_E$.</p>
    <p><span class="tinh">FIND:</span> Signature pair $(r, s)$, certificate $\text{Cert}$, and verification $v_1 == v_2$.</p>
    <p><span class="st">STEPS:</span></p>
    <ul>
      <li><span class="st">Step 1 (Check $k_E$):</span> Compute <span class="kw">$\gcd(k_E, p - 1)$</span>.
        <br>• If $\gcd \ne 1 \implies$ <b>NO SOLUTION</b> ($k_E^{-1}$ does not exist).
        <br>• If $\gcd = 1 \implies$ Proceed to Step 2.
      </li>
      <li><span class="st">Step 2 (Compute $r$):</span> <span class="f">$r = \alpha^{k_E} \pmod p$</span> (via Square-and-Multiply).</li>
      <li><span class="st">Step 3 (Find $k_E^{-1}$):</span> Use EEA table to compute <span class="f">$k_E^{-1} \pmod{p - 1}$</span>.</li>
      <li><span class="st">Step 4 (Compute $s$):</span> <span class="f">$s = (x - d \cdot r) \cdot k_E^{-1} \pmod{p - 1}$</span>.
        <br>• If $(x - d \cdot r) < 0 \implies$ add $p-1$: <span class="f">$((x - dr) \bmod (p-1) + (p-1)) \bmod (p-1)$</span>.
        <br>$\implies$ Signature: <span class="f">$(r, s)$</span>. Certificate: <span class="f">$\text{Cert} = (x, (r, s))$</span>.
      </li>
      <li><span class="st">Step 5 (Verification):</span>
        <br>• Compute <span class="f">$v_1 = [(\beta^r \bmod p) \cdot (r^s \bmod p)] \pmod p$</span>.
        <br>• Compute <span class="f">$v_2 = \alpha^x \pmod p$</span>. Check: <span class="kw">$v_1 \equiv v_2 \pmod p$</span> $\implies$ Valid!
      </li>
    </ul>
  </div>

  <!-- FORM 10: DSA SIGNATURE -->
  <div class="box">
    <div class="box-title">FORM 10: DSA (DIGITAL SIGNATURE ALGORITHM)</div>
    <p><span class="cho">GIVEN:</span> $p, q \mid (p-1)$, $\alpha$ of order $q$ ($\alpha^q \equiv 1 \bmod p$), private $d \in [1, q-1] \implies \beta = \alpha^d \pmod p$, hash $h = H(M)$, ephemeral key $k_E \in [1, q-1]$.</p>
    <p><span class="tinh">FIND:</span> DSA signature pair $(r, s)$ and verification equality $v == r$.</p>
    <p><span class="st">STEPS:</span></p>
    <ul>
      <li><span class="st">Signing (4 steps):</span>
        <br>1. Check condition <span class="kw">$\gcd(k_E, q) = 1$</span>.
        <br>2. Compute <span class="f">$r = (\alpha^{k_E} \bmod p) \bmod q$</span> (if $r=0 \to$ re-select $k_E$).
        <br>3. Compute modular inverse mod $q$: <span class="f">$k_E^{-1} \pmod q$</span> (EEA with $q$).
        <br>4. Compute <span class="f">$s = k_E^{-1} \cdot (h + d \cdot r) \pmod q$</span> $\implies$ Signature <span class="f">$(r, s)$</span>.
      </li>
      <li><span class="st">Verification (5 steps):</span>
        <br>1. Check valid bounds: $0 < r < q$ and $0 < s < q$.
        <br>2. Compute inverse: <span class="f">$w = s^{-1} \pmod q$</span> (EEA with $q$).
        <br>3. Compute: <span class="f">$u_1 = (h \cdot w) \pmod q$</span> and <span class="f">$u_2 = (r \cdot w) \pmod q$</span>.
        <br>4. Compute: <span class="f">$v = [(\alpha^{u_1} \cdot \beta^{u_2}) \bmod p] \bmod q$</span>.
        <br>5. Check: If <span class="kw">$v == r$</span> $\implies$ Signature is valid!
      </li>
    </ul>
  </div>

  <!-- FORM 11: DIFFIE-HELLMAN KEY EXCHANGE -->
  <div class="box">
    <div class="box-title">FORM 11: DIFFIE-HELLMAN KEY EXCHANGE (DHKE)</div>
    <p><span class="cho">GIVEN:</span> Public params $p, \alpha$; Alice private $a$, Bob private $b$ (Oscar $o$).</p>
    <p><span class="tinh">FIND:</span> Public keys $k_A, k_B$, shared session key $k_{AB}$, MITM attack keys.</p>
    <p><span class="st">STEPS:</span></p>
    <ul>
      <li><span class="st">Step 1:</span> Alice computes public key: <span class="f">$k_A = \alpha^a \pmod p$</span> $\to$ sends to Bob.</li>
      <li><span class="st">Step 2:</span> Bob computes public key: <span class="f">$k_B = \alpha^b \pmod p$</span> $\to$ sends to Alice.</li>
      <li><span class="st">Step 3:</span> Compute shared key: Alice computes <span class="f">$k_{AB} = (k_B)^a \pmod p$</span>; Bob computes <span class="f">$k_{AB} = (k_A)^b \pmod p$</span>.</li>
      <li><span class="st">Step 4:</span> Consistency check: <span class="f">$k_{AB} = \alpha^{a \cdot b} \pmod p$</span>.</li>
      <li><span class="st">Step 5 (MITM Attack):</span> Oscar intercepts $k_A, k_B$, sends fake $k_O = \alpha^o \pmod p$:
        <br>Alice-Oscar key: <span class="f">$k_{AO} = k_O^a \pmod p$</span> | Bob-Oscar key: <span class="f">$k_{BO} = k_O^b \pmod p$</span>.
      </li>
    </ul>
  </div>

  <!-- FORM 12: A5/1 STREAM CIPHER -->
  <div class="box">
    <div class="box-title">FORM 12: A5/1 STREAM CIPHER (GSM ENCRYPTION)</div>
    <p><span class="cho">GIVEN:</span> 3 LFSRs: $R_1(19b, C_1=8)$, $R_2(22b, C_2=10)$, $R_3(23b, C_3=10)$; bit $m_j$.</p>
    <p><span class="tinh">FIND:</span> Majority $maj$, clocked LFSRs, keystream bit $s_j$, ciphertext $c_j$.</p>
    <p><span class="st">STEPS:</span></p>
    <ul>
      <li><span class="st">Step 1 (Majority bit):</span> <span class="f">$maj(C_1, C_2, C_3) = (C_1 C_2) \oplus (C_1 C_3) \oplus (C_2 C_3)$</span> (rule: bit value occurring $\ge 2$ times).</li>
      <li><span class="st">Step 2 (Clocking rule):</span> Registers with $C_i == maj \implies$ CLOCKED (shift right 1 bit, insert feedback XOR at bit 0); $C_i \ne maj \implies$ FROZEN.</li>
      <li><span class="st">Step 3 (Keystream bit):</span> <span class="f">$s_j = R_1[\text{MSB}] \oplus R_2[\text{MSB}] \oplus R_3[\text{MSB}]$</span>.</li>
      <li><span class="st">Step 4:</span> Encrypt: <span class="f">$c_j = m_j \oplus s_j$</span> | Decrypt: <span class="f">$m_j = c_j \oplus s_j$</span>.</li>
    </ul>
  </div>

  <!-- FORM 13: SHA-1 PADDING & DAVIES-MEYER -->
  <div class="box">
    <div class="box-title">FORM 13: SHA-1 PADDING & DAVIES-MEYER HASH</div>
    <p><span class="cho">GIVEN:</span> Original message bit-length $l$.</p>
    <p><span class="tinh">FIND:</span> Number of padding zero bits ($k$), total length $L$, blocks $N = L/512$.</p>
    <p><span class="st">STEPS:</span></p>
    <ul>
      <li><span class="st">Step 1:</span> Initial length: $l$ bits. Append a single '1' bit $\to l + 1$ bits.</li>
      <li><span class="st">Step 2:</span> Append $k$ '0' bits such that: <span class="f">$(l + 1 + k) \equiv 448 \pmod{512}$</span>
        <br>$\implies \mathbf{k = (447 - (l \bmod 512)) \bmod 512}$ (where $0 \le k < 512$).
      </li>
      <li><span class="st">Step 3:</span> Append 64-bit binary representation of $l$ (Big-Endian).</li>
      <li><span class="st">Step 4:</span> Total length: <span class="f">$L = l + 1 + k + 64$</span>. Total 512-bit blocks: <span class="f">$N = L / 512$</span>.</li>
      <li><span class="st">Davies-Meyer:</span> <span class="f">$h_i = E_{m_i}(h_{i-1}) \oplus h_{i-1}$</span> ($m_i$ = Key, $h_{i-1}$ = Plaintext).
        <br>Birthday Paradox: Collision resistance security for $n$-bit hash is <span class="kw">$\mathcal{O}(2^{n/2})$</span>.
      </li>
    </ul>
  </div>

</div>

</div>
