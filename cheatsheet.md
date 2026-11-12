<style>
@page {
  size: A4 portrait;
  margin: 3.5mm 5mm 3.5mm 5mm;
}
@media print {
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    font-size: 6.7pt;
    line-height: 1.16;
    color: #000;
    background: #fff;
    margin: 0;
    padding: 0;
  }
  h1 { 
    font-size: 8.8pt; 
    margin: 0 0 1px 0; 
    text-align: center; 
    font-weight: 800; 
    color: #1e3a8a; 
    text-transform: uppercase; 
    border-bottom: 1.2px solid #1e3a8a; 
    padding-bottom: 1px; 
  }
  .meta-sub {
    font-size: 6.2pt;
    text-align: center;
    color: #475569;
    font-weight: 700;
    margin-bottom: 2px;
  }
  .grid-3col { 
    display: grid; 
    grid-template-columns: 1fr 1fr 1fr; 
    column-gap: 3mm; 
    row-gap: 1.8mm; 
  }
  .box { 
    border: 0.8px solid #475569; 
    border-radius: 2px; 
    padding: 2px 3px; 
    background: #fff; 
    break-inside: avoid;
    margin-bottom: 1.8mm;
  }
  .box-title { 
    font-size: 7pt; 
    font-weight: 800; 
    color: #0f172a; 
    background: #f1f5f9; 
    margin: -2px -3px 2px -3px; 
    padding: 1.2px 3px; 
    border-bottom: 0.8px solid #94a3b8; 
    text-transform: uppercase;
  }
  .f { 
    font-family: "Courier New", Consolas, monospace; 
    font-weight: 700; 
    color: #1d4ed8; 
    font-size: 6.8pt; 
  }
  .st { font-weight: 800; color: #047857; }
  .kw { font-weight: 800; color: #b91c1c; }
  table.eea { 
    width: 100%; 
    border-collapse: collapse; 
    font-size: 6.1pt; 
    margin: 1.5px 0; 
  }
  table.eea th, table.eea td { 
    border: 0.5px solid #64748b; 
    padding: 0.6px 1px; 
    text-align: center; 
  }
  table.eea th { 
    background: #f8fafc; 
    font-weight: 700; 
  }
  ul { margin: 0; padding-left: 9px; }
  li { margin-bottom: 0.8px; }
  p { margin: 0.8px 0; }
}
@media screen {
  body { font-family: sans-serif; font-size: 11px; line-height: 1.35; padding: 15px; max-width: 1200px; margin: 0 auto; }
  .grid-3col { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 10px; }
  .box { border: 1px solid #cbd5e1; border-radius: 4px; padding: 8px; margin-bottom: 8px; }
  .box-title { font-weight: bold; background: #f1f5f9; padding: 4px; margin: -8px -8px 6px -8px; }
  table.eea { width: 100%; border-collapse: collapse; margin: 4px 0; font-size: 10px; }
  table.eea th, table.eea td { border: 1px solid #cbd5e1; padding: 3px; text-align: center; }
  .f { font-family: monospace; font-weight: bold; color: #1d4ed8; }
  .st { font-weight: bold; color: #047857; }
  .kw { font-weight: bold; color: #b91c1c; }
}
</style>

# USTH CRYPTOGRAPHY - CÔNG THỨC & CÁC BƯỚC GIẢI TỰ LUẬN TẤT CẢ DẠNG BÀI THI (A4)
<div class="meta-sub">Dành cho phòng thi | Cấu trúc chuẩn từng bước để viết bài thi | Không ghim số cố định | Tính số qua Tool</div>

<div class="grid-3col">

<!-- ==================== CỘT 1: S-BOX, EEA, SQUARE-AND-MULTIPLY ==================== -->
<div class="col">

  <!-- DẠNG 1: S-BOX DES -->
  <div class="box">
    <div class="box-title">DẠNG 1: TRA CỨU HỘP S-BOX DES S1 (3 ĐIỂM)</div>
    <ul>
      <li><span class="st">Bước 1:</span> Rút gọn số: <span class="f">$x = (\text{Mã\_SV}) \pmod{64}$</span> (với $0 \le x < 64$).</li>
      <li><span class="st">Bước 2:</span> Đổi $x$ ra nhị phân 6 bit: <span class="f">$x = (b_1 b_2 b_3 b_4 b_5 b_6)_2$</span>.</li>
      <li><span class="st">Bước 3:</span> Xác định tọa độ Hàng và Cột:
        <br>• <b>Hàng $r$:</b> Ghép bit đầu và cuối: <span class="f">$r = (b_1 b_6)_2 \in \{0, 1, 2, 3\}$</span>.
        <br>• <b>Cột $c$:</b> Ghép 4 bit ở giữa: <span class="f">$c = (b_2 b_3 b_4 b_5)_2 \in \{0 \dots 15\}$</span>.
      </li>
      <li><span class="st">Bước 4:</span> Gióng hàng $r$ và cột $c$ trên bảng ma trận $S_1$ đề cho:
        <br>$\implies \mathbf{\text{Giá trị}} = S_1[r][c]$ (hệ thập phân).
      </li>
      <li><span class="st">Bước 5:</span> Đổi giá trị sang nhị phân 4 bit: <span class="f">$(y_1 y_2 y_3 y_4)_2$</span>.
        <br><i>Ghi chú:</i> Nếu số lẻ $\to$ đề Question Set 1; Chẵn $\to$ Set 2.
      </li>
    </ul>
  </div>

  <!-- DẠNG 2: THUẬT TOÁN EEA LẬP BẢNG -->
  <div class="box">
    <div class="box-title">DẠNG 2: BẢNG EUCLID MỞ RỘNG (EEA) TÌM NGHỊCH ĐẢO</div>
    <p><b>Bài toán:</b> Tìm <span class="f">$d = e^{-1} \pmod m$</span> sao cho <span class="f">$e \cdot d \equiv 1 \pmod m$</span>.</p>
    <ul>
      <li><span class="st">Bước 1:</span> Lập bảng mẫu gồm 6 cột: <code>Bước | q | r | s | t | Phương trình chia</code>.</li>
      <li><span class="st">Bước 2:</span> Điền 2 dòng khởi tạo (init):
        <br>• Dòng 1 (init): $r_0 = m$, $s_0 = 1$, $t_0 = 0$. (PT: $r_0 = m$).
        <br>• Dòng 2 (init): $r_1 = e$, $s_1 = 0$, $t_1 = 1$. (PT: $r_1 = e$).
      </li>
      <li><span class="st">Bước 3:</span> Tính từng dòng $i \ge 1$ theo công thức truy hồi:
        <table class="eea">
          <tr><th>q</th><th>r</th><th>s</th><th>t</th><th>Phương trình chia</th></tr>
          <tr><td>$q_i = \lfloor r_{i-2} / r_{i-1} \rfloor$</td><td>$r_i = r_{i-2} - q_i r_{i-1}$</td><td>$s_i = s_{i-2} - q_i s_{i-1}$</td><td>$t_i = t_{i-2} - q_i t_{i-1}$</td><td>$r_{i-2} = q_i \cdot r_{i-1} + r_i$</td></tr>
        </table>
      </li>
      <li><span class="st">Bước 4:</span> Dừng khi $r_i = 0$. Dòng trước đó $r_{i-1} = \gcd(e, m) = 1$.</li>
      <li><span class="st">Bước 5:</span> Kết luận: <span class="f">$d \equiv t_{i-1} \pmod m$</span>.
        <br><b>Nếu $t_{i-1} < 0$:</b> Tính <span class="kw">$d = t_{i-1} + m$</span>.
        <br>Kiểm tra lại: <span class="f">$(e \cdot d) \pmod m = 1$</span>.
      </li>
    </ul>
  </div>

  <!-- DẠNG 3: SQUARE-AND-MULTIPLY -->
  <div class="box">
    <div class="box-title">DẠNG 3: LŨY THỪA NHANH (SQUARE-AND-MULTIPLY)</div>
    <p><b>Bài toán:</b> Tính giá trị <span class="f">$y = x^c \pmod n$</span> (ví dụ $M^e \bmod N$ hay $C^d \bmod N$).</p>
    <ul>
      <li><span class="st">Bước 1:</span> Đổi số mũ $c$ ra dạng nhị phân: <span class="f">$c = (b_k b_{k-1} \dots b_1 b_0)_2$</span>.</li>
      <li><span class="st">Bước 2:</span> Kẻ bảng gồm 5 cột:
        <br><code>Bước | Bit b_i | Phép toán | Biểu thức tính toán | Giá trị y</code>.
      </li>
      <li><span class="st">Bước 3:</span> Khởi tạo $y = 1$. Quét từ bit cao nhất $b_k$ về $b_0$:
        <br>• <b>Mọi bit:</b> Luôn thực hiện <span class="f">Square: $y = y^2 \pmod n$</span>.
        <br>• <b>Nếu bit $b_i = 1$:</b> Thực hiện thêm <span class="f">Multiply: $y = (y \cdot x) \pmod n$</span>.
      </li>
      <li><span class="st">Bước 4:</span> Giá trị $y$ ở dòng cuối cùng chính là đáp số của phép tính.</li>
    </ul>
  </div>

</div>

<!-- ==================== CỘT 2: RSA, CHỨNG CHỈ PKI, EMAIL ==================== -->
<div class="col">

  <!-- DẠNG 4: THIẾT LẬP KHÓA RSA -->
  <div class="box">
    <div class="box-title">DẠNG 4: THIẾT LẬP KHÓA RSA (KEY GENERATION)</div>
    <ul>
      <li><span class="st">Bước 1:</span> Đề cho 2 số nguyên tố $p, q$. Tính Modulus:
        <br><span class="f">$N = p \cdot q$</span>.
      </li>
      <li><span class="st">Bước 2:</span> Tính giá trị hàm Euler Totient:
        <br><span class="f">$\Phi(N) = (p - 1)(q - 1)$</span>.
      </li>
      <li><span class="st">Bước 3:</span> Chọn số mũ công khai $e$:
        <br>• Điều kiện: $1 < e < \Phi(N)$ và <span class="kw">$\gcd(e, \Phi(N)) = 1$</span>.
        <br>• Phân tích thừa số nguyên tố $\Phi(N)$ để chỉ ra $e$ nguyên tố cùng nhau với $\Phi(N)$.
      </li>
      <li><span class="st">Bước 4:</span> Tìm số mũ bí mật $d$ bằng thuật toán EEA:
        <br><span class="f">$d = e^{-1} \pmod{\Phi(N)} \iff e \cdot d \equiv 1 \pmod{\Phi(N)}$</span>.
      </li>
      <li><span class="st">Bước 5:</span> Kết luận cặp khóa:
        <br>• Khóa công khai (Public Key): <span class="f">$k_{pub} = (N, e)$</span>.
        <br>• Khóa bí mật (Private Key): <span class="f">$k_{pri} = (N, d)$</span>.
      </li>
    </ul>
  </div>

  <!-- DẠNG 5: MÃ HÓA & GIẢI MÃ RSA -->
  <div class="box">
    <div class="box-title">DẠNG 5: MÃ HÓA & GIẢI MÃ RSA (ENCRYPT/DECRYPT)</div>
    <ul>
      <li><span class="st">Bước 1 (Mã hóa - Encryption):</span>
        <br>• Công thức: <span class="f">$C = M^e \pmod N$</span> (với $0 \le M < N$).
        <br>• Trình bày bảng tính lũy thừa nhanh Square-and-Multiply cho $M^e \pmod N$.
        <br>$\implies$ Kết luận bản mã $C$ thu được.
      </li>
      <li><span class="st">Bước 2 (Giải mã - Decryption):</span>
        <br>• Công thức: <span class="f">$M = C^d \pmod N$</span>.
        <br>• Trình bày bảng tính lũy thừa nhanh Square-and-Multiply cho $C^d \pmod N$.
        <br>$\implies$ Kết luận bản rõ $M$ khôi phục.
      </li>
      <li><span class="st">Bước 3 (Kiểm tra xác thực):</span>
        <br>So sánh bản rõ khôi phục với bản rõ gốc: <span class="kw">$M_{dec} == M$</span>.
        <br>Giải thích: Do $C^d \equiv (M^e)^d \equiv M^{e \cdot d} \equiv M^{k\Phi(N)+1} \equiv M \pmod N$.
      </li>
    </ul>
  </div>

  <!-- DẠNG 6: CHỨNG CHỈ RSA & HYBRID EMAIL -->
  <div class="box">
    <div class="box-title">DẠNG 6: CHỨNG CHỈ RSA CA & GỬI EMAIL PKI</div>
    <p><b>A. Cấp & Xác thực Chứng chỉ số RSA:</b></p>
    <ul>
      <li><span class="st">B1 (Ký số CA):</span> CA ký lên thông tin người dùng $M$ bằng khóa bí mật CA $d_{CA}$: <span class="f">$S_{CA} = M^{d_{CA}} \pmod{N_{CA}}$</span>.</li>
      <li><span class="st">B2 (Đóng gói Cert):</span> $\text{Cert}_A = (M, S_{CA}, e_A, N_A)$.</li>
      <li><span class="st">B3 (Xác thực Cert):</span> Người nhận dùng khóa công khai CA $e_{CA}$ tính: <span class="f">$V = (S_{CA})^{e_{CA}} \pmod{N_{CA}}$</span>. Kiểm tra nếu <span class="kw">$V == M$</span> $\to$ Chứng chỉ hợp lệ.</li>
    </ul>
    <p><b>B. Quy trình Gửi nhận Email bảo mật PKI (Hybrid):</b></p>
    <ul>
      <li><span class="st">Phía gửi Alice (5 bước):</span>
        <br>1. Tạo khóa phiên đối xứng ngẫu nhiên $K_{sym}$ (AES/DES).
        <br>2. Mã hóa thư: <span class="f">$C = E_{K_{sym}}(\text{Email})$</span>.
        <br>3. Mã hóa khóa phiên bằng khóa Bob: <span class="f">$C_K = E_{e_B}(K_{sym}) = K_{sym}^{e_B} \pmod{N_B}$</span>.
        <br>4. Ký số băm thư bằng khóa Alice: <span class="f">$\sigma = S_{d_A}(\text{Hash}(\text{Email})) = \text{Hash}^{d_A} \pmod{N_A}$</span>.
        <br>5. Đóng gói gửi cho Bob: $\{C, C_K, \sigma, \text{Cert}_A\}$.
      </li>
      <li><span class="st">Phía nhận Bob (3 bước):</span>
        <br>1. Dùng $d_B$ giải mã $C_K \implies$ thu được khóa phiên $K_{sym}$.
        <br>2. Dùng $K_{sym}$ giải mã $C \implies$ đọc được nội dung Email.
        <br>3. Lấy $e_A$ từ $\text{Cert}_A$ để xác thực chữ ký $\sigma \implies$ tính toàn vẹn.
      </li>
    </ul>
  </div>

</div>

<!-- ==================== CỘT 3: ELGAMAL, DHKE, SHA-1 ==================== -->
<div class="col">

  <!-- DẠNG 7: CHỮ KÝ SỐ ELGAMAL -->
  <div class="box">
    <div class="box-title">DẠNG 7: CHỮ KÝ SỐ ELGAMAL & CHỨNG CHỈ CA</div>
    <p><b>Tham số:</b> Số nguyên tố $p$, phần tử sinh $\alpha$, khóa bí mật $d \implies$ Khóa công khai: <span class="f">$\beta = \alpha^d \pmod p$</span>. Thông điệp cần ký $x$ (hoặc $x_A = x + e_A$).</p>
    <ul>
      <li><span class="st">Bước 1 (Kiểm tra khóa tạm thời $k_E$):</span>
        <br>• Tính <span class="kw">$\gcd(k_E, p - 1)$</span>.
        <br>• <b>Nếu $\gcd \ne 1$:</b> Kết luận <span class="kw">VÔ NGHIỆM</span> (do không tồn tại nghịch đảo $k_E^{-1}$).
        <br>• <b>Nếu $\gcd = 1$:</b> Thỏa mãn, tiếp tục bước 2.
      </li>
      <li><span class="st">Bước 2 (Tính thành phần $r$):</span>
        <br><span class="f">$r = \alpha^{k_E} \pmod p$</span> (tính bằng Square-and-Multiply).
      </li>
      <li><span class="st">Bước 3 (Tìm nghịch đảo $k_E^{-1}$):</span>
        <br>Lập bảng EEA tính <span class="f">$k_E^{-1} \pmod{p - 1}$</span> sao cho $k_E \cdot k_E^{-1} \equiv 1 \pmod{p-1}$.
      </li>
      <li><span class="st">Bước 4 (Tính thành phần $s$):</span>
        <br><span class="f">$s = (x - d \cdot r) \cdot k_E^{-1} \pmod{p - 1}$</span>.
        <br>• Nếu $(x - d \cdot r) < 0$: Quy về phần dư dương bằng công thức:
        <br><span class="f">$((x - d \cdot r) \pmod{p-1} + (p-1)) \pmod{p-1}$</span>.
        <br>$\implies$ Kết luận chữ ký số: <span class="f">$(r, s)$</span>. Chứng chỉ: <span class="f">$\text{Cert} = (x, (r, s))$</span>.
      </li>
      <li><span class="st">Bước 5 (Xác minh chữ ký - Verification):</span>
        <br>• Tính <span class="f">$v_1 = (\beta^r \cdot r^s) \pmod p = [(\beta^r \bmod p) \cdot (r^s \bmod p)] \pmod p$</span>.
        <br>• Tính <span class="f">$v_2 = \alpha^x \pmod p$</span>.
        <br>• So sánh: Nếu <span class="kw">$v_1 \equiv v_2 \pmod p$</span> $\implies$ Chữ ký hoàn toàn hợp lệ!
      </li>
    </ul>
  </div>

  <!-- DẠNG 8: TRAO ĐỔI KHÓA DIFFIE-HELLMAN -->
  <div class="box">
    <div class="box-title">DẠNG 8: TRAO ĐỔI KHÓA DIFFIE-HELLMAN (DHKE)</div>
    <ul>
      <li><span class="st">Bước 1:</span> Tham số công khai hệ thống: Số nguyên tố $p$, phần tử sinh $\alpha \in \mathbb{Z}_p^*$.</li>
      <li><span class="st">Bước 2:</span> Alice chọn số bí mật $a$. Tính khóa công khai:
        <br><span class="f">$k_A = \alpha^a \pmod p$</span> $\implies$ gửi $k_A$ cho Bob.
      </li>
      <li><span class="st">Bước 3:</span> Bob chọn số bí mật $b$. Tính khóa công khai:
        <br><span class="f">$k_B = \alpha^b \pmod p$</span> $\implies$ gửi $k_B$ cho Alice.
      </li>
      <li><span class="st">Bước 4:</span> Tính khóa phiên bí mật chung (Session Key):
        <br>• Alice tính: <span class="f">$k_{AB} = (k_B)^a \pmod p$</span>.
        <br>• Bob tính: <span class="f">$k_{AB} = (k_A)^b \pmod p$</span>.
        <br>• Kiểm tra tính thống nhất: <span class="f">$k_{AB} = \alpha^{a \cdot b} \pmod p$</span> (Hai bên ra cùng số).
      </li>
      <li><span class="st">Bước 5 (Nếu đề hỏi Tấn công MITM của Oscar):</span>
        <br>• Oscar chọn bí mật $o$, tính $k_O = \alpha^o \pmod p$ gửi cho cả hai.
        <br>• Khóa Alice - Oscar: <span class="f">$k_{AO} = (k_O)^a = (k_A)^o \pmod p$</span>.
        <br>• Khóa Bob - Oscar: <span class="f">$k_{BO} = (k_O)^b = (k_B)^o \pmod p$</span>.
      </li>
    </ul>
  </div>

  <!-- DẠNG 9: TIỀN XỬ LÝ ĐỆM SHA-1 -->
  <div class="box">
    <div class="box-title">DẠNG 9: ĐỆM SHA-1 & HÀM BĂM KHỐI DAVIES-MEYER</div>
    <ul>
      <li><span class="st">Bước 1:</span> Xác định chiều dài ban đầu: $l$ bits.</li>
      <li><span class="st">Bước 2 (Chèn bit 1):</span> Thêm 1 bit '1' vào đuôi thông điệp ($l + 1$ bits).</li>
      <li><span class="st">Bước 3 (Tính số bit 0 cần đệm $k$):</span>
        <br>• Điều kiện: <span class="f">$(l + 1 + k) \equiv 448 \pmod{512}$</span>.
        <br>• Công thức: <span class="f">$k = (447 - (l \bmod 512)) \pmod{512}$</span> (với $0 \le k < 512$).
        <br><i>Cách tính nhẩm:</i> Lấy $l \pmod{512} = \text{rem}$. Nếu $\text{rem} \le 447 \implies k = 447 - \text{rem}$; Nếu $\text{rem} > 447 \implies k = 447 - \text{rem} + 512$.
      </li>
      <li><span class="st">Bước 4 (Chèn 64 bit độ dài gốc):</span> Biểu diễn $l$ bằng 64 bit nhị phân.</li>
      <li><span class="st">Bước 5 (Tổng kết):</span>
        <br>• Tổng chiều dài sau đệm: <span class="f">$L = l + 1 + k + 64$</span> bits.
        <br>• Số khối 512-bit: <span class="f">$N = L / 512$</span> (khối).
      </li>
      <li><span class="st">Sơ đồ khối Davies-Meyer (nếu đề hỏi):</span>
        <br><span class="f">$h_i = E_{m_i}(h_{i-1}) \oplus h_{i-1}$</span> (Khối $m_i$ làm Khóa, $h_{i-1}$ làm Bản rõ).
      </li>
    </ul>
  </div>

</div>

</div>
