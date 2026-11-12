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

# USTH CRYPTOGRAPHY - TỔNG HỢP CÔNG THỨC & CÁC BƯỚC GIẢI MỌI DẠNG BÀI THI (A4)
<div class="meta-sub">Dành cho phòng thi | Cấu trúc chuẩn từng bước để viết bài thi | Không ghim số cố định | Tính số qua Tool</div>

<div class="grid-3col">

<!-- ==================== CỘT 1: NỀN TẢNG TÍNH TOÁN & CỔ ĐIỂN ==================== -->
<div class="col">

  <!-- DẠNG 1: S-BOX DES -->
  <div class="box">
    <div class="box-title">DẠNG 1: TRA CỨU HỘP S-BOX DES S1 (3 ĐIỂM)</div>
    <p><span class="cho">CHO:</span> Mã SV (hoặc số thập phân $x_{raw}$), bảng tra $S_1$ (4 hàng $\times$ 16 cột).</p>
    <p><span class="tinh">TÍNH:</span> Giá trị đầu ra 4 bit $(y_1 y_2 y_3 y_4)_2$ và giá trị thập phân.</p>
    <p><span class="st">CÁC BƯỚC TÍNH:</span></p>
    <ul>
      <li><span class="st">B1:</span> Rút gọn: <span class="f">$x = (\text{Mã\_SV}) \pmod{64}$</span> ($0 \le x < 64$).</li>
      <li><span class="st">B2:</span> Đổi $x \to$ nhị phân 6 bit: <span class="f">$x = (b_1 b_2 b_3 b_4 b_5 b_6)_2$</span>.</li>
      <li><span class="st">B3:</span> Tọa độ Hàng & Cột:
        <br>• <b>Hàng $r$:</b> Ghép bit đầu và cuối: <span class="f">$r = (b_1 b_6)_2 \in \{0, 1, 2, 3\}$</span>.
        <br>• <b>Cột $c$:</b> Ghép 4 bit ở giữa: <span class="f">$c = (b_2 b_3 b_4 b_5)_2 \in \{0 \dots 15\}$</span>.
      </li>
      <li><span class="st">B4:</span> Gióng ma trận đề cho: <span class="f">$\text{Val} = S_1[r][c]$</span> (hệ thập phân).
        <br><i>Ghi chú:</i> Số lẻ $\to$ chọn Set 1; Chẵn $\to$ chọn Set 2 (đề 2023).
      </li>
      <li><span class="st">B5:</span> Đổi $\text{Val} \to$ nhị phân 4 bit: <span class="f">$(y_1 y_2 y_3 y_4)_2$</span>.</li>
    </ul>
  </div>

  <!-- DẠNG 2: BẢNG EEA -->
  <div class="box">
    <div class="box-title">DẠNG 2: BẢNG EUCLID MỞ RỘNG (EEA) TÌM NGHỊCH ĐẢO</div>
    <p><span class="cho">CHO:</span> Số $e$ (hoặc $a$) và modulo $m$ (thỏa mãn $\gcd(e, m) = 1$).</p>
    <p><span class="tinh">TÍNH:</span> Nghịch đảo modulo <span class="f">$d = e^{-1} \pmod m$</span> sao cho <span class="f">$e \cdot d \equiv 1 \pmod m$</span>.</p>
    <p><span class="st">CÁC BƯỚC TÍNH:</span></p>
    <ul>
      <li><span class="st">B1:</span> Kẻ bảng 6 cột: <code>Bước | q | r | s | t | Phương trình chia</code>.</li>
      <li><span class="st">B2:</span> 2 dòng khởi tạo (init):
        <br>• Dòng 0: $r_0 = m$, $s_0 = 1$, $t_0 = 0$. (PT: $r_0 = m$).
        <br>• Dòng 1: $r_1 = e$, $s_1 = 0$, $t_1 = 1$. (PT: $r_1 = e$).
      </li>
      <li><span class="st">B3:</span> Tính từng dòng $i \ge 2$ theo công thức truy hồi:
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
    <p><span class="cho">CHO:</span> Cơ số $x$, số mũ $c$ (lớn), modulo $n$.</p>
    <p><span class="tinh">TÍNH:</span> Giá trị lũy thừa dư <span class="f">$y = x^c \pmod n$</span>.</p>
    <p><span class="st">CÁC BƯỚC TÍNH:</span></p>
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
    <p><b>A. Hệ mật cổ điển (Cho bản rõ $P$, Khóa $K \implies$ Tính mã $C$ & giải $P$):</b></p>
    <ul>
      <li><b>Caesar:</b> Mã hóa $C = (P + k) \pmod{26}$ | Giải mã $P = (C - k) \pmod{26}$.</li>
      <li><b>Affine:</b> $C = (aP + b) \pmod{26}$ (ĐK: $\gcd(a, 26) = 1$).
        <br>Giải mã: <span class="f">$P = a^{-1}(C - b) \pmod{26}$</span> (tìm $a^{-1} \pmod{26}$ bằng EEA).
      </li>
      <li><b>Vigenère:</b> Lặp khóa $K$: $C_i = (P_i + K_i) \pmod{26}$ | $P_i = (C_i - K_i) \pmod{26}$.</li>
      <li><b>OTP / Vernam:</b> $C = P \oplus K$ | $P = C \oplus K$ (Bảo mật hoàn hảo).</li>
    </ul>
    <p><b>B. Định lý số dư Trung Hoa (CRT):</b></p>
    <p><span class="cho">CHO:</span> Hệ đồng dư $x \equiv a_i \pmod{m_i}$ với $\gcd(m_i, m_j) = 1$.</p>
    <p><span class="tinh">TÍNH:</span> Nghiệm duy nhất <span class="f">$x \pmod M$</span>.</p>
    <ul>
      <li><span class="st">B1:</span> Tính tích $M = \prod m_i = m_1 \cdot m_2 \cdots m_k$.</li>
      <li><span class="st">B2:</span> Tính $M_i = M/m_i$ và tìm nghịch đảo $y_i = M_i^{-1} \pmod{m_i}$ (EEA).</li>
      <li><span class="st">B3:</span> Nghiệm duy nhất: <span class="f">$x = \left(\sum a_i M_i y_i\right) \pmod M$</span>.</li>
    </ul>
  </div>

</div>

<!-- ==================== CỘT 2: RSA, CHỨNG CHỈ PKI, BLOCK CIPHERS ==================== -->
<div class="col">

  <!-- DẠNG 5: THIẾT LẬP KHÓA RSA -->
  <div class="box">
    <div class="box-title">DẠNG 5: THIẾT LẬP KHÓA RSA (KEY GENERATION)</div>
    <p><span class="cho">CHO:</span> Hai số nguyên tố $p, q$ (hoặc cho $N, p \implies q = N/p$).</p>
    <p><span class="tinh">TÍNH:</span> Khóa công khai <span class="f">$k_{pub} = (N, e)$</span> và Khóa bí mật <span class="f">$k_{pri} = (N, d)$</span>.</p>
    <p><span class="st">CÁC BƯỚC TÍNH:</span></p>
    <ul>
      <li><span class="st">B1:</span> Tính Modulus: <span class="f">$N = p \cdot q$</span>.</li>
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
    <p><span class="cho">CHO:</span> Bản rõ $M$ ($0 \le M < N$), khóa công khai $(N, e)$, khóa bí mật $(N, d)$.</p>
    <p><span class="tinh">TÍNH:</span> Bản mã $C$ và khôi phục bản rõ $M_{dec}$.</p>
    <p><span class="st">CÁC BƯỚC TÍNH:</span></p>
    <ul>
      <li><span class="st">B1 (Mã hóa):</span> <span class="f">$C = M^e \pmod N$</span>.
        <br>Kẻ bảng Square-and-Multiply cho $M^e \pmod N \implies$ Bản mã $C$.
      </li>
      <li><span class="st">B2 (Giải mã):</span> <span class="f">$M = C^d \pmod N$</span>.
        <br>Kẻ bảng Square-and-Multiply cho $C^d \pmod N \implies$ Bản rõ $M$.
      </li>
      <li><span class="st">B3 (Kiểm tra & CM):</span> So sánh <span class="kw">$M_{dec} == M$</span>.
        <br>Chứng minh: $C^d \equiv (M^e)^d \equiv M^{k\Phi(N)+1} \equiv M \pmod N$ (Euler).
      </li>
    </ul>
  </div>

  <!-- DẠNG 7: CHỨNG CHỈ RSA & HYBRID EMAIL -->
  <div class="box">
    <div class="box-title">DẠNG 7: CHỨNG CHỈ RSA CA & GỬI EMAIL PKI</div>
    <p><b>A. Chứng chỉ số RSA CA:</b></p>
    <p><span class="cho">CHO:</span> Thông điệp/khóa $M$, khóa bí mật CA $d_{CA}$, khóa công khai CA $(N_{CA}, e_{CA})$.</p>
    <p><span class="tinh">TÍNH:</span> Chữ ký CA $S_{CA}$ và xác minh tính hợp lệ.</p>
    <ul>
      <li><span class="st">Ký số CA:</span> <span class="f">$S_{CA} = M^{d_{CA}} \pmod{N_{CA}}$</span>. Đóng gói $\text{Cert}_A = (M, S_{CA})$.</li>
      <li><span class="st">Xác thực:</span> Tính <span class="f">$V = (S_{CA})^{e_{CA}} \pmod{N_{CA}}$</span>. So sánh <span class="kw">$V == M$</span>.</li>
    </ul>
    <p><b>B. Quy trình Gửi nhận Email bảo mật PKI (Hybrid):</b></p>
    <p><span class="cho">CHO:</span> Thư $P$, cặp khóa Alice $(e_A, d_A)$, Bob $(e_B, d_B)$, $\text{Cert}_A$.</p>
    <p><span class="tinh">TÍNH:</span> Các gói tin mã hóa gửi đi và các bước khôi phục phía Bob.</p>
    <ul>
      <li><span class="st">Alice gửi (5 bước):</span>
        <br>1. Sinh khóa phiên đối xứng ngẫu nhiên $K_{sym}$ (AES/DES).
        <br>2. Mã hóa thư: <span class="f">$C = E_{K_{sym}}(P)$</span>.
        <br>3. Mã hóa khóa phiên: <span class="f">$C_K = K_{sym}^{e_B} \pmod{N_B}$</span>.
        <br>4. Ký số băm thư: <span class="f">$\sigma = (H(P))^{d_A} \pmod{N_A}$</span>.
        <br>5. Đóng gói gửi cho Bob: $\{C, C_K, \sigma, \text{Cert}_A\}$.
      </li>
      <li><span class="st">Bob nhận (3 bước):</span>
        <br>1. Dùng $d_B$ giải mã $C_K \implies$ thu được khóa $K_{sym} = C_K^{d_B} \pmod{N_B}$.
        <br>2. Dùng $K_{sym}$ giải mã $C \implies$ lấy lại nội dung thư $P = D_{K_{sym}}(C)$.
        <br>3. Lấy $e_A$ từ $\text{Cert}_A$ kiểm tra <span class="kw">$\sigma^{e_A} \pmod{N_A} == H(P)$</span>.
      </li>
    </ul>
  </div>

  <!-- DẠNG 8: BLOCK CIPHER MODES & FEISTEL -->
  <div class="box">
    <div class="box-title">DẠNG 8: CHẾ ĐỘ MÃ KHỐI & MẠNG FEISTEL (DES/AES)</div>
    <p><b>A. Các chế độ hoạt động mã hóa khối:</b></p>
    <p><span class="cho">CHO:</span> Các khối bản rõ $P_i$, khóa đối xứng $K$, vector khởi tạo IV.</p>
    <p><span class="tinh">TÍNH:</span> Bản mã $C_i$ (hoặc giải mã bản rõ $P_i$):</p>
    <ul>
      <li><b>ECB:</b> $C_i = E_K(P_i)$ | $P_i = D_K(C_i)$. Không dùng IV $\implies$ rò rỉ mẫu.</li>
      <li><b>CBC:</b> $C_0 = \text{IV}$; $C_i = E_K(P_i \oplus C_{i-1})$. Giải mã: <span class="f">$P_i = D_K(C_i) \oplus C_{i-1}$</span>.</li>
      <li><b>CFB:</b> $C_0 = \text{IV}$; $C_i = P_i \oplus E_K(C_{i-1})$. Giải mã: <span class="f">$P_i = C_i \oplus E_K(C_{i-1})$</span>.</li>
      <li><b>OFB:</b> $S_0 = \text{IV}$; $S_i = E_K(S_{i-1})$; $C_i = P_i \oplus S_i$. Giải mã: <span class="f">$P_i = C_i \oplus S_i$</span>.</li>
      <li><b>CTR:</b> $S_i = E_K(\text{IV} \mathbin{\Vert} i)$; $C_i = P_i \oplus S_i$. Giải mã song song.</li>
    </ul>
    <p><b>B. Mạng Feistel (DES):</b></p>
    <p><span class="cho">CHO:</span> Khối 64 bit $(L_{i-1}, R_{i-1})$, hàm vòng $F$, khóa con $K_i$.</p>
    <p><span class="tinh">TÍNH:</span> Đầu ra vòng $i$ $(L_i, R_i)$ và công thức giải mã ngược:</p>
    <ul>
      <li>Mã hóa vòng $i$: <span class="f">$L_i = R_{i-1}$</span> ; <span class="f">$R_i = L_{i-1} \oplus F(R_{i-1}, K_i)$</span>.</li>
      <li>Giải mã (đảo thứ tự $K_{16} \to K_1$): <span class="f">$R_{i-1} = L_i$</span> ; <span class="f">$L_{i-1} = R_i \oplus F(L_i, K_i)$</span>.</li>
    </ul>
  </div>

</div>

<!-- ==================== CỘT 3: ELGAMAL, DSA, DHKE, A5/1, SHA-1 ==================== -->
<div class="col">

  <!-- DẠNG 9: CHỮ KÝ SỐ ELGAMAL -->
  <div class="box">
    <div class="box-title">DẠNG 9: CHỮ KÝ SỐ ELGAMAL & CHỨNG CHỈ CA</div>
    <p><span class="cho">CHO:</span> Nguyên tố $p$, phần tử sinh $\alpha$, khóa bí mật $d \implies \beta = \alpha^d \pmod p$, thông điệp $x$ (hoặc $x_A = x + e_A$), khóa tạm $k_E$.</p>
    <p><span class="tinh">TÍNH:</span> Cặp chữ ký $(r, s)$, chứng chỉ $\text{Cert}$ và xác thực $v_1 == v_2$.</p>
    <p><span class="st">CÁC BƯỚC TÍNH:</span></p>
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
      <li><span class="st">B5 (Xác thực):</span>
        <br>• Tính <span class="f">$v_1 = [(\beta^r \bmod p) \cdot (r^s \bmod p)] \pmod p$</span>.
        <br>• Tính <span class="f">$v_2 = \alpha^x \pmod p$</span>. So sánh: <span class="kw">$v_1 \equiv v_2 \pmod p$</span> $\implies$ Hợp lệ!
      </li>
    </ul>
  </div>

  <!-- DẠNG 10: CHỮ KÝ SỐ DSA -->
  <div class="box">
    <div class="box-title">DẠNG 10: CHỮ KÝ SỐ DSA (DIGITAL SIGNATURE ALGORITHM)</div>
    <p><span class="cho">CHO:</span> $p, q \mid (p-1)$, $\alpha$ bậc $q$ ($\alpha^q \equiv 1 \bmod p$), bí mật $d \in [1, q-1] \implies \beta = \alpha^d \pmod p$, hash $h = H(M)$, khóa tạm $k_E \in [1, q-1]$.</p>
    <p><span class="tinh">TÍNH:</span> Cặp chữ ký DSA $(r, s)$ và các bước kiểm tra xác minh $v == r$.</p>
    <p><span class="st">CÁC BƯỚC TÍNH:</span></p>
    <ul>
      <li><span class="st">Ký số (Signing - 4 bước):</span>
        <br>1. Kiểm tra <span class="kw">$\gcd(k_E, q) = 1$</span>.
        <br>2. Tính <span class="f">$r = (\alpha^{k_E} \bmod p) \bmod q$</span> (nếu $r=0 \to$ chọn lại $k_E$).
        <br>3. Tìm nghịch đảo modulo $q$: <span class="f">$k_E^{-1} \pmod q$</span> (EEA với $q$).
        <br>4. Tính <span class="f">$s = k_E^{-1} \cdot (h + d \cdot r) \pmod q$</span> $\implies$ Chữ ký <span class="f">$(r, s)$</span>.
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
    <p><span class="cho">CHO:</span> Tham số công khai $p, \alpha$; bí mật Alice $a$, bí mật Bob $b$ (Oscar $o$).</p>
    <p><span class="tinh">TÍNH:</span> Khóa công khai $k_A, k_B$, khóa phiên $k_{AB}$, khóa tấn công MITM.</p>
    <p><span class="st">CÁC BƯỚC TÍNH:</span></p>
    <ul>
      <li><span class="st">B1:</span> Alice tính <span class="f">$k_A = \alpha^a \pmod p$</span> $\to$ gửi Bob.</li>
      <li><span class="st">B2:</span> Bob tính <span class="f">$k_B = \alpha^b \pmod p$</span> $\to$ gửi Alice.</li>
      <li><span class="st">B3:</span> Tính khóa chung: Alice tính <span class="f">$k_{AB} = (k_B)^a \pmod p$</span>; Bob tính <span class="f">$k_{AB} = (k_A)^b \pmod p$</span>.</li>
      <li><span class="st">B4:</span> Kiểm tra tính thống nhất: <span class="f">$k_{AB} = \alpha^{a \cdot b} \pmod p$</span>.</li>
      <li><span class="st">B5 (Tấn công MITM):</span> Oscar gửi $k_O = \alpha^o \pmod p$:
        <br>Khóa Alice-Oscar: <span class="f">$k_{AO} = k_O^a \pmod p$</span> | Bob-Oscar: <span class="f">$k_{BO} = k_O^b \pmod p$</span>.
      </li>
    </ul>
  </div>

  <!-- DẠNG 12: MÃ DÒNG A5/1 -->
  <div class="box">
    <div class="box-title">DẠNG 12: MÃ DÒNG A5/1 (GSM STREAM CIPHER)</div>
    <p><span class="cho">CHO:</span> 3 LFSR: $R_1(19b, C_1=8)$, $R_2(22b, C_2=10)$, $R_3(23b, C_3=10)$; bit rõ $m_j$.</p>
    <p><span class="tinh">TÍNH:</span> Bit $maj$, các LFSR được clock, bit dòng khóa $s_j$, bản mã $c_j$.</p>
    <p><span class="st">CÁC BƯỚC TÍNH:</span></p>
    <ul>
      <li><span class="st">B1 (Bit đa số):</span> <span class="f">$maj(C_1, C_2, C_3) = (C_1 C_2) \oplus (C_1 C_3) \oplus (C_2 C_3)$</span> (nhẩm: bit xuất hiện $\ge 2$ lần).</li>
      <li><span class="st">B2 (Quy tắc Clock):</span> Thanh ghi nào có $C_i == maj \implies$ ĐƯỢC CLOCK (dịch phải 1 bit, nạp bit 0 là XOR tap bits); $C_i \ne maj$ GIỮ NGUYÊN.</li>
      <li><span class="st">B3 (Xuất bit dòng khóa):</span> <span class="f">$s_j = R_1[\text{MSB}] \oplus R_2[\text{MSB}] \oplus R_3[\text{MSB}]$</span>.</li>
      <li><span class="st">B4:</span> Mã hóa: <span class="f">$c_j = m_j \oplus s_j$</span> | Giải mã: <span class="f">$m_j = c_j \oplus s_j$</span>.</li>
    </ul>
  </div>

  <!-- DẠNG 13: ĐỆM SHA-1 & DAVIES-MEYER -->
  <div class="box">
    <div class="box-title">DẠNG 13: ĐỆM SHA-1 & HÀM BĂM KHỐI DAVIES-MEYER</div>
    <p><span class="cho">CHO:</span> Chiều dài thông điệp ban đầu $l$ bits.</p>
    <p><span class="tinh">TÍNH:</span> Số bit '0' đệm ($k$), tổng độ dài $L$, số khối $N = L/512$, sơ đồ băm.</p>
    <p><span class="st">CÁC BƯỚC TÍNH:</span></p>
    <ul>
      <li><span class="st">B1:</span> Chiều dài ban đầu: $l$ bits. Nối thêm 1 bit '1' $\to l + 1$ bits.</li>
      <li><span class="st">B2:</span> Thêm $k$ bit '0' sao cho: <span class="f">$(l + 1 + k) \equiv 448 \pmod{512}$</span>
        <br>$\implies \mathbf{k = (447 - (l \bmod 512)) \bmod 512}$ (với $0 \le k < 512$).
      </li>
      <li><span class="st">B3:</span> Nối thêm 64 bit biểu diễn nhị phân của chiều dài $l$ (Big-Endian).</li>
      <li><span class="st">B4:</span> Tổng bit: <span class="f">$L = l + 1 + k + 64$</span>. Số khối 512-bit: <span class="f">$N = L / 512$</span>.</li>
      <li><span class="st">Davies-Meyer:</span> <span class="f">$h_i = E_{m_i}(h_{i-1}) \oplus h_{i-1}$</span> ($m_i$ là Khóa, $h_{i-1}$ là Bản rõ).
        <br>Birthday Paradox: Độ an toàn tìm va chạm hàm băm $n$-bit là <span class="kw">$\mathcal{O}(2^{n/2})$</span>.
      </li>
    </ul>
  </div>

</div>

</div>
