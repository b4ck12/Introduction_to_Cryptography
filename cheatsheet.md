<style>
@page {
  size: A4 portrait;
  margin: 2.5mm 3.5mm 2.5mm 3.5mm;
}
@media print {
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    font-size: 5.9pt;
    line-height: 1.12;
    color: #000;
    background: #fff;
    margin: 0;
    padding: 0;
  }
  h1 { 
    font-size: 8pt; 
    margin: 0 0 1px 0; 
    text-align: center; 
    font-weight: 800; 
    color: #1e3a8a; 
    text-transform: uppercase; 
    border-bottom: 0.8px solid #1e3a8a; 
    padding-bottom: 0.5px; 
  }
  .meta-sub {
    font-size: 5.4pt;
    text-align: center;
    color: #475569;
    font-weight: 700;
    margin-bottom: 1px;
  }
  .grid-3col { 
    display: grid; 
    grid-template-columns: 1fr 1fr 1fr; 
    column-gap: 2.2mm; 
    row-gap: 1mm; 
  }
  .box { 
    border: 0.6px solid #475569; 
    border-radius: 1.5px; 
    padding: 1.2px 2mm; 
    background: #fff; 
    break-inside: avoid;
    margin-bottom: 1mm;
  }
  .box-title { 
    font-size: 6.2pt; 
    font-weight: 800; 
    color: #0f172a; 
    background: #f1f5f9; 
    margin: -1.2px -2mm 1.2px -2mm; 
    padding: 0.8px 2mm; 
    border-bottom: 0.5px solid #94a3b8; 
    text-transform: uppercase;
  }
  .f { 
    font-family: "Courier New", Consolas, monospace; 
    font-weight: 700; 
    color: #1d4ed8; 
    font-size: 6.0pt; 
  }
  .st { font-weight: 800; color: #047857; }
  .kw { font-weight: 800; color: #b91c1c; }
  table.eea { 
    width: 100%; 
    border-collapse: collapse; 
    font-size: 5.5pt; 
    margin: 0.8px 0; 
  }
  table.eea th, table.eea td { 
    border: 0.4px solid #64748b; 
    padding: 0.3px 0.6px; 
    text-align: center; 
  }
  table.eea th { 
    background: #f8fafc; 
    font-weight: 700; 
  }
  ul { margin: 0; padding-left: 7.5px; }
  li { margin-bottom: 0.4px; }
  p { margin: 0.4px 0; }
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
}
</style>

# USTH CRYPTOGRAPHY - TỔNG HỢP CÔNG THỨC & CÁC BƯỚC GIẢI MỌI DẠNG BÀI THI (A4)
<div class="meta-sub">Dành cho phòng thi | Cấu trúc chuẩn từng bước để viết bài thi | Không ghim số cố định | Tính số qua Tool</div>

<div class="grid-3col">

<!-- ==================== CỘT 1: NỀN TẢNG TÍNH TOÁN & CỔ ĐIỂN ==================== -->
<div class="col">

  <!-- DẠNG 1: S-BOX DES -->
  <div class="box">
    <div class="box-title">DẠNG 1: TRA CỨU HỘP S-BOX DES S1 (3 ĐIỂM)</div>
    <ul>
      <li><span class="st">B1:</span> Rút gọn: <span class="f">$x = (\text{Mã\_SV}) \pmod{64}$</span> ($0 \le x < 64$).</li>
      <li><span class="st">B2:</span> Đổi $x \to$ nhị phân 6 bit: <span class="f">$x = (b_1 b_2 b_3 b_4 b_5 b_6)_2$</span>.</li>
      <li><span class="st">B3:</span> Tọa độ Hàng & Cột:
        <br>• <b>Hàng $r$:</b> Ghép bit đầu và cuối: <span class="f">$r = (b_1 b_6)_2 \in \{0, 1, 2, 3\}$</span>.
        <br>• <b>Cột $c$:</b> Ghép 4 bit ở giữa: <span class="f">$c = (b_2 b_3 b_4 b_5)_2 \in \{0 \dots 15\}$</span>.
      </li>
      <li><span class="st">B4:</span> Gióng ma trận đề cho: <span class="f">$\text{Val} = S_1[r][c]$</span> (hệ thập phân).</li>
      <li><span class="st">B5:</span> Đổi $\text{Val} \to$ nhị phân 4 bit: <span class="f">$(y_1 y_2 y_3 y_4)_2$</span>.
        <br><i>Ghi chú:</i> Số lẻ $\to$ chọn Set 1; Chẵn $\to$ Set 2 (đề 2023).
      </li>
    </ul>
  </div>

  <!-- DẠNG 2: BẢNG EEA -->
  <div class="box">
    <div class="box-title">DẠNG 2: BẢNG EUCLID MỞ RỘNG (EEA) TÌM NGHỊCH ĐẢO</div>
    <p><b>Bài toán:</b> Tìm <span class="f">$d = e^{-1} \pmod m$</span> sao cho <span class="f">$e \cdot d \equiv 1 \pmod m$</span>.</p>
    <ul>
      <li><span class="st">B1:</span> Kẻ bảng 6 cột: <code>Bước | q | r | s | t | Phương trình chia</code>.</li>
      <li><span class="st">B2:</span> 2 dòng khởi tạo (init):
        <br>• Dòng 1: $r_0 = m$, $s_0 = 1$, $t_0 = 0$. (PT: $r_0 = m$).
        <br>• Dòng 2: $r_1 = e$, $s_1 = 0$, $t_1 = 1$. (PT: $r_1 = e$).
      </li>
      <li><span class="st">B3:</span> Tính từng dòng $i \ge 1$ theo công thức truy hồi:
        <table class="eea">
          <tr><th>q</th><th>r</th><th>s</th><th>t</th><th>Phương trình chia</th></tr>
          <tr><td>$q_i = \lfloor r_{i-2} / r_{i-1} \rfloor$</td><td>$r_i = r_{i-2} - q_i r_{i-1}$</td><td>$s_i = s_{i-2} - q_i s_{i-1}$</td><td>$t_i = t_{i-2} - q_i t_{i-1}$</td><td>$r_{i-2} = q_i \cdot r_{i-1} + r_i$</td></tr>
        </table>
      </li>
      <li><span class="st">B4:</span> Dừng khi $r_i = 0$. Dòng trước cho $\gcd(e, m) = r_{i-1} = 1$.</li>
      <li><span class="st">B5:</span> Lấy <span class="f">$d \equiv t_{i-1} \pmod m$</span>. Nếu $t_{i-1} < 0 \implies \mathbf{d = t_{i-1} + m}$.</li>
    </ul>
  </div>

  <!-- DẠNG 3: SQUARE-AND-MULTIPLY -->
  <div class="box">
    <div class="box-title">DẠNG 3: LŨY THỪA NHANH (SQUARE-AND-MULTIPLY)</div>
    <p><b>Bài toán:</b> Tính giá trị <span class="f">$y = x^c \pmod n$</span> (với số mũ $c$ lớn).</p>
    <ul>
      <li><span class="st">B1:</span> Đổi số mũ sang nhị phân: <span class="f">$c = (b_k b_{k-1} \dots b_1 b_0)_2$</span>.</li>
      <li><span class="st">B2:</span> Kẻ bảng 5 cột: <code>Bước | Bit b_i | Phép toán | Tính toán | Giá trị y</code>.</li>
      <li><span class="st">B3:</span> Khởi tạo $y = 1$. Quét từ bit $b_k$ về $b_0$:
        <br>• <b>Mọi bit:</b> Luôn tính <span class="f">Square: $y = y^2 \pmod n$</span>.
        <br>• <b>Nếu bit $b_i = 1$:</b> Nhân thêm: <span class="f">Multiply: $y = (y \cdot x) \pmod n$</span>.
      </li>
      <li><span class="st">B4:</span> Giá trị $y$ ở dòng cuối chính là đáp số của phép tính.</li>
    </ul>
  </div>

  <!-- DẠNG 4: MẬT MÃ CỔ ĐIỂN & CRT -->
  <div class="box">
    <div class="box-title">DẠNG 4: MẬT MÃ CỔ ĐIỂN & ĐỊNH LÝ SỐ DƯ (CRT)</div>
    <ul>
      <li><b>Caesar:</b> Mã hóa $C = (P + k) \pmod{26}$ | Giải mã $P = (C - k) \pmod{26}$.</li>
      <li><b>Affine:</b> $C = (aP + b) \pmod{26}$ (ĐK: $\gcd(a, 26) = 1$).
        <br>Giải mã: <span class="f">$P = a^{-1}(C - b) \pmod{26}$</span> (tìm $a^{-1} \pmod{26}$ bằng EEA).
      </li>
      <li><b>Vigenère:</b> Lặp khóa $K$: $C_i = (P_i + K_i) \pmod{26}$ | $P_i = (C_i - K_i) \pmod{26}$.</li>
      <li><b>One-Time Pad / XOR:</b> $C = P \oplus K$ | $P = C \oplus K$ (Bảo mật hoàn hảo).</li>
      <li><b>Định lý số dư Trung Hoa (CRT):</b> Hệ $x \equiv a_i \pmod{m_i}$ ($\gcd(m_i, m_j)=1$).
        <br>1. Tính tích $M = \prod m_i$.
        <br>2. Tính $M_i = M/m_i$ và tìm nghịch đảo $y_i = M_i^{-1} \pmod{m_i}$ (EEA).
        <br>3. Nghiệm duy nhất: <span class="f">$x = \left(\sum a_i M_i y_i\right) \pmod M$</span>.
      </li>
    </ul>
  </div>

</div>

<!-- ==================== CỘT 2: RSA, CHỨNG CHỈ PKI, BLOCK CIPHERS ==================== -->
<div class="col">

  <!-- DẠNG 5: THIẾT LẬP KHÓA RSA -->
  <div class="box">
    <div class="box-title">DẠNG 5: THIẾT LẬP KHÓA RSA (KEY GENERATION)</div>
    <ul>
      <li><span class="st">B1:</span> Đề cho 2 số nguyên tố $p, q$. Tính Modulus: <span class="f">$N = p \cdot q$</span>.</li>
      <li><span class="st">B2:</span> Tính hàm Euler: <span class="f">$\Phi(N) = (p - 1)(q - 1)$</span>.</li>
      <li><span class="st">B3:</span> Chọn số mũ công khai $e$:
        <br>• Điều kiện: $1 < e < \Phi(N)$ và <span class="kw">$\gcd(e, \Phi(N)) = 1$</span>.
        <br>• Phân tích thừa số $\Phi(N)$ để chứng minh $e$ nguyên tố cùng nhau.
      </li>
      <li><span class="st">B4:</span> Tìm số mũ bí mật $d$ bằng thuật toán EEA (Dạng 2):
        <br><span class="f">$d = e^{-1} \pmod{\Phi(N)} \iff e \cdot d \equiv 1 \pmod{\Phi(N)}$</span>.
      </li>
      <li><span class="st">B5:</span> Kết luận cặp khóa:
        <br>• Public Key: <span class="f">$k_{pub} = (N, e)$</span> | Private Key: <span class="f">$k_{pri} = (N, d)$</span>.
      </li>
    </ul>
  </div>

  <!-- DẠNG 6: MÃ HÓA & GIẢI MÃ RSA -->
  <div class="box">
    <div class="box-title">DẠNG 6: MÃ HÓA & GIẢI MÃ RSA (ENCRYPT/DECRYPT)</div>
    <ul>
      <li><span class="st">B1 (Mã hóa):</span> <span class="f">$C = M^e \pmod N$</span> (với $0 \le M < N$).
        <br>Kẻ bảng Square-and-Multiply cho $M^e \pmod N \implies$ Bản mã $C$.
      </li>
      <li><span class="st">B2 (Giải mã):</span> <span class="f">$M = C^d \pmod N$</span>.
        <br>Kẻ bảng Square-and-Multiply cho $C^d \pmod N \implies$ Bản rõ $M$.
      </li>
      <li><span class="st">B3:</span> Kiểm tra: <span class="kw">$M_{dec} == M$</span>.
        <br>Chứng minh: $C^d \equiv (M^e)^d \equiv M^{k\Phi(N)+1} \equiv M \pmod N$ (Euler).
      </li>
    </ul>
  </div>

  <!-- DẠNG 7: CHỨNG CHỈ RSA & HYBRID EMAIL -->
  <div class="box">
    <div class="box-title">DẠNG 7: CHỨNG CHỈ RSA CA & GỬI EMAIL PKI</div>
    <p><b>A. Cấp & Xác thực Chứng chỉ số RSA:</b></p>
    <ul>
      <li><span class="st">Ký số CA:</span> CA ký lên ID/khóa $M$ bằng $d_{CA}$: <span class="f">$S_{CA} = M^{d_{CA}} \pmod{N_{CA}}$</span>.</li>
      <li><span class="st">Đóng gói:</span> $\text{Cert}_A = (M, S_{CA}, e_A, N_A)$.</li>
      <li><span class="st">Xác thực:</span> Tính <span class="f">$V = (S_{CA})^{e_{CA}} \pmod{N_{CA}}$</span>. So sánh <span class="kw">$V == M$</span>.</li>
    </ul>
    <p><b>B. Quy trình Gửi nhận Email bảo mật PKI (Hybrid):</b></p>
    <ul>
      <li><span class="st">Alice gửi (5 bước):</span>
        <br>1. Sinh khóa phiên đối xứng ngẫu nhiên $K_{sym}$ (AES/DES).
        <br>2. Mã hóa thư: <span class="f">$C = E_{K_{sym}}(\text{Email})$</span>.
        <br>3. Mã hóa khóa phiên: <span class="f">$C_K = E_{e_B}(K_{sym}) = K_{sym}^{e_B} \pmod{N_B}$</span>.
        <br>4. Ký số băm thư: <span class="f">$\sigma = S_{d_A}(\text{Hash}(\text{Email})) = \text{Hash}^{d_A} \pmod{N_A}$</span>.
        <br>5. Đóng gói gửi cho Bob: $\{C, C_K, \sigma, \text{Cert}_A\}$.
      </li>
      <li><span class="st">Bob nhận (3 bước):</span>
        <br>1. Dùng $d_B$ giải mã $C_K \implies$ thu được khóa $K_{sym}$.
        <br>2. Dùng $K_{sym}$ giải mã $C \implies$ lấy lại nội dung Email.
        <br>3. Lấy $e_A$ từ $\text{Cert}_A$ xác thực chữ ký $\sigma \implies$ toàn vẹn.
      </li>
    </ul>
  </div>

  <!-- DẠNG 8: BLOCK CIPHER MODES & FEISTEL -->
  <div class="box">
    <div class="box-title">DẠNG 8: CHẾ ĐỘ MÃ KHỐI & MẠNG FEISTEL (DES/AES)</div>
    <p><b>A. Các chế độ hoạt động mã hóa khối (Modes of Operation):</b></p>
    <ul>
      <li><b>ECB:</b> $C_i = E_K(P_i)$ | $P_i = D_K(C_i)$. Không dùng IV $\implies$ rò rỉ mẫu.</li>
      <li><b>CBC:</b> $C_0 = \text{IV}$; $C_i = E_K(P_i \oplus C_{i-1})$. Giải mã: <span class="f">$P_i = D_K(C_i) \oplus C_{i-1}$</span>.</li>
      <li><b>CFB:</b> $C_0 = \text{IV}$; $C_i = P_i \oplus E_K(C_{i-1})$. Giải mã: <span class="f">$P_i = C_i \oplus E_K(C_{i-1})$</span>.</li>
      <li><b>OFB:</b> $S_0 = \text{IV}$; $S_i = E_K(S_{i-1})$; $C_i = P_i \oplus S_i$. Giải mã: <span class="f">$P_i = C_i \oplus S_i$</span>.</li>
      <li><b>CTR:</b> $S_i = E_K(\text{IV} \mathbin{\Vert} i)$; $C_i = P_i \oplus S_i$. Cho phép song song hóa.</li>
    </ul>
    <p><b>B. Mạng Feistel (DES):</b> Khối 64 bit $\to (L_{i-1}, R_{i-1})$:
      <br>• Vòng $i$: <span class="f">$L_i = R_{i-1}$</span> ; <span class="f">$R_i = L_{i-1} \oplus F(R_{i-1}, K_i)$</span>.
      <br>• Giải mã: Đảo ngược khóa con ($K_{16} \to K_1$): <span class="f">$R_{i-1} = L_i$</span> ; <span class="f">$L_{i-1} = R_i \oplus F(L_i, K_i)$</span>.
    </p>
  </div>

</div>

<!-- ==================== CỘT 3: ELGAMAL, DSA, DHKE, A5/1, SHA-1 ==================== -->
<div class="col">

  <!-- DẠNG 9: CHỮ KÝ SỐ ELGAMAL -->
  <div class="box">
    <div class="box-title">DẠNG 9: CHỮ KÝ SỐ ELGAMAL & CHỨNG CHỈ CA</div>
    <p><b>Tham số CA:</b> Nguyên tố $p$, phần tử sinh $\alpha$, khóa bí mật $d \implies$ Public: <span class="f">$\beta = \alpha^d \pmod p$</span>. Thông điệp $x$ (hoặc $x_A = x + e_A$).</p>
    <ul>
      <li><span class="st">B1 (Kiểm tra $k_E$):</span> Tính <span class="kw">$\gcd(k_E, p - 1)$</span>.
        <br>• Nếu $\gcd \ne 1 \implies$ <b>VÔ NGHIỆM</b> (không tồn tại $k_E^{-1}$).
        <br>• Nếu $\gcd = 1 \implies$ Tiếp tục bước 2.
      </li>
      <li><span class="st">B2 (Tính $r$):</span> <span class="f">$r = \alpha^{k_E} \pmod p$</span> (tính bằng Sq-and-Mul).</li>
      <li><span class="st">B3 (Tìm $k_E^{-1}$):</span> Lập bảng EEA tính <span class="f">$k_E^{-1} \pmod{p - 1}$</span>.</li>
      <li><span class="st">B4 (Tính $s$):</span> <span class="f">$s = (x - d \cdot r) \cdot k_E^{-1} \pmod{p - 1}$</span>.
        <br>• Nếu $(x - d \cdot r) < 0 \implies$ cộng $p-1$: <span class="f">$((x - dr) \bmod (p-1) + (p-1)) \bmod (p-1)$</span>.
        <br>$\implies$ Cặp chữ ký: <span class="f">$(r, s)$</span>. Cert: <span class="f">$\text{Cert} = (x, (r, s))$</span>.
      </li>
      <li><span class="st">B5 (Xác thực - Verification):</span>
        <br>• Tính <span class="f">$v_1 = (\beta^r \cdot r^s) \pmod p = [(\beta^r \bmod p) \cdot (r^s \bmod p)] \pmod p$</span>.
        <br>• Tính <span class="f">$v_2 = \alpha^x \pmod p$</span>. So sánh: <span class="kw">$v_1 \equiv v_2 \pmod p$</span> $\implies$ Hợp lệ!
      </li>
    </ul>
  </div>

  <!-- DẠNG 10: CHỮ KÝ SỐ DSA -->
  <div class="box">
    <div class="box-title">DẠNG 10: CHỮ KÝ SỐ DSA (DIGITAL SIGNATURE ALGORITHM)</div>
    <p><b>Tham số:</b> Nguyên tố $p$, ước nguyên tố $q \mid (p-1)$, phần tử sinh $\alpha$ bậc $q$ ($\alpha^q \equiv 1 \bmod p$), khóa bí mật $d \in [1, q-1] \implies$ Khóa công khai: <span class="f">$\beta = \alpha^d \pmod p$</span>. Hash $h = H(M)$.</p>
    <ul>
      <li><span class="st">Ký số (Signing - 4 bước):</span>
        <br>1. Chọn ngẫu nhiên khóa tạm $k_E \in [1, q-1]$ thỏa <span class="kw">$\gcd(k_E, q) = 1$</span>.
        <br>2. Tính <span class="f">$r = (\alpha^{k_E} \bmod p) \bmod q$</span> (nếu $r=0 \to$ chọn lại $k_E$).
        <br>3. Tìm nghịch đảo modulo $q$: <span class="f">$k_E^{-1} \pmod q$</span> (EEA với $q$).
        <br>4. Tính <span class="f">$s = k_E^{-1} \cdot (h + d \cdot r) \pmod q$</span> (nếu $s=0 \to$ chọn lại $k_E$).
        <br>$\implies$ Cặp chữ ký DSA là <span class="f">$(r, s)$</span>.
      </li>
      <li><span class="st">Xác minh (Verification - 5 bước):</span>
        <br>1. Kiểm tra điều kiện hợp lệ: $0 < r < q$ và $0 < s < q$.
        <br>2. Tính nghịch đảo: <span class="f">$w = s^{-1} \pmod q$</span> (EEA với $q$).
        <br>3. Tính: <span class="f">$u_1 = (h \cdot w) \pmod q$</span> và <span class="f">$u_2 = (r \cdot w) \pmod q$</span>.
        <br>4. Tính: <span class="f">$v = [(\alpha^{u_1} \cdot \beta^{u_2}) \bmod p] \bmod q$</span>.
        <br>5. So sánh: Nếu <span class="kw">$v == r$</span> $\implies$ Chữ ký hoàn toàn hợp lệ!
      </li>
    </ul>
  </div>

  <!-- DẠNG 11: TRAO ĐỔI KHÓA DIFFIE-HELLMAN -->
  <div class="box">
    <div class="box-title">DẠNG 11: TRAO ĐỔI KHÓA DIFFIE-HELLMAN (DHKE)</div>
    <ul>
      <li><span class="st">B1:</span> Tham số công khai hệ thống: Nguyên tố $p$, phần tử sinh $\alpha$.</li>
      <li><span class="st">B2:</span> Alice chọn bí mật $a \implies$ Tính <span class="f">$k_A = \alpha^a \pmod p$</span> $\to$ gửi Bob.</li>
      <li><span class="st">B3:</span> Bob chọn bí mật $b \implies$ Tính <span class="f">$k_B = \alpha^b \pmod p$</span> $\to$ gửi Alice.</li>
      <li><span class="st">B4:</span> Tính khóa phiên chung: Alice tính <span class="f">$k_{AB} = (k_B)^a \pmod p$</span>; Bob tính <span class="f">$k_{AB} = (k_A)^b \pmod p$</span>. Kiểm tra: <span class="f">$k_{AB} = \alpha^{a \cdot b} \pmod p$</span>.</li>
      <li><span class="st">B5 (Tấn công MITM):</span> Oscar chặn $k_A, k_B$, gửi $k_O = \alpha^o \pmod p$:
        <br>Khóa Alice-Oscar: <span class="f">$k_{AO} = k_O^a$</span> | Bob-Oscar: <span class="f">$k_{BO} = k_O^b$</span>.
      </li>
    </ul>
  </div>

  <!-- DẠNG 12: MÃ DÒNG A5/1 -->
  <div class="box">
    <div class="box-title">DẠNG 12: MÃ DÒNG A5/1 (GSM STREAM CIPHER)</div>
    <p><b>Cấu trúc 3 LFSR:</b> $R_1(19b, C_1=8)$, $R_2(22b, C_2=10)$, $R_3(23b, C_3=10)$.</p>
    <ul>
      <li><span class="st">B1 (Đa số - Majority):</span> <span class="f">$maj(C_1, C_2, C_3) = (C_1 C_2) \oplus (C_1 C_3) \oplus (C_2 C_3)$</span>.
        <br><i>Nhẩm nhanh:</i> Giá trị bit 0 hoặc 1 nào xuất hiện $\ge 2$ lần thì là $maj$.
      </li>
      <li><span class="st">B2 (Quy tắc Clock):</span> Thanh ghi nào có $C_i == maj$ $\implies$ ĐƯỢC CLOCK (dịch phải 1 bit, nạp bit 0 là XOR tap bits); $C_i \ne maj$ GIỮ NGUYÊN.</li>
      <li><span class="st">B3 (Xuất bit dòng khóa):</span> <span class="f">$s_j = R_1[\text{MSB}] \oplus R_2[\text{MSB}] \oplus R_3[\text{MSB}]$</span>.</li>
      <li><span class="st">B4:</span> Mã hóa: <span class="f">$c_j = m_j \oplus s_j$</span> | Giải mã: <span class="f">$m_j = c_j \oplus s_j$</span>.</li>
    </ul>
  </div>

  <!-- DẠNG 13: ĐỆM SHA-1 & DAVIES-MEYER -->
  <div class="box">
    <div class="box-title">DẠNG 13: ĐỆM SHA-1 & HÀM BĂM KHỐI DAVIES-MEYER</div>
    <ul>
      <li><span class="st">B1:</span> Chiều dài ban đầu: $l$ bits.</li>
      <li><span class="st">B2:</span> Nối 1 bit '1' vào đuôi thông điệp ($l + 1$ bits).</li>
      <li><span class="st">B3:</span> Thêm $k$ bit '0' sao cho: <span class="f">$(l + 1 + k) \equiv 448 \pmod{512}$</span>
        <br>$\implies \mathbf{k = (447 - (l \bmod 512)) \bmod 512}$ (với $0 \le k < 512$).
      </li>
      <li><span class="st">B4:</span> Nối 64 bit biểu diễn nhị phân của chiều dài $l$ (Big-Endian).</li>
      <li><span class="st">B5:</span> Tổng bit: <span class="f">$L = l + 1 + k + 64$</span>. Số khối 512-bit: <span class="f">$N = L / 512$</span>.</li>
      <li><span class="st">Davies-Meyer:</span> <span class="f">$h_i = E_{m_i}(h_{i-1}) \oplus h_{i-1}$</span> ($m_i$ là Khóa, $h_{i-1}$ là Bản rõ).
        <br>Birthday Paradox: Độ an toàn tìm va chạm hàm băm $n$-bit là <span class="kw">$\mathcal{O}(2^{n/2})$</span>.
      </li>
    </ul>
  </div>

</div>

</div>
