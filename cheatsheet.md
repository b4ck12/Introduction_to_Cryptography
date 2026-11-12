<style>
@page {
  size: A4 portrait;
  margin: 4mm 5mm 4mm 5mm;
}
@media print {
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    font-size: 6.8pt;
    line-height: 1.18;
    color: #050505;
    background: #fff;
    margin: 0;
    padding: 0;
  }
  h1 { 
    font-size: 9pt; 
    margin: 0 0 1px 0; 
    text-align: center; 
    font-weight: 800; 
    color: #1e3a8a; 
    text-transform: uppercase; 
    border-bottom: 1.2px solid #1e3a8a; 
    padding-bottom: 1px; 
    letter-spacing: 0.3px;
  }
  .meta-sub {
    font-size: 6.5pt;
    text-align: center;
    color: #475569;
    font-weight: 600;
    margin-bottom: 2.5px;
  }
  .grid-3col { 
    display: grid; 
    grid-template-columns: 1fr 1fr 1fr; 
    column-gap: 3.5mm; 
    row-gap: 2mm; 
  }
  .box { 
    border: 0.8px solid #64748b; 
    border-radius: 2px; 
    padding: 2px 3.5px; 
    background: #fff; 
    break-inside: avoid;
    margin-bottom: 2mm;
  }
  .box-title { 
    font-size: 7.2pt; 
    font-weight: 800; 
    color: #0f172a; 
    background: #f1f5f9; 
    margin: -2px -3.5px 2px -3.5px; 
    padding: 1.5px 3.5px; 
    border-bottom: 0.8px solid #94a3b8; 
    text-transform: uppercase;
  }
  .formula { 
    font-family: "Courier New", Consolas, monospace; 
    font-weight: 700; 
    color: #1d4ed8; 
    font-size: 6.9pt; 
  }
  .keyword { font-weight: 700; color: #b91c1c; }
  .step { font-weight: 700; color: #047857; }
  table.eea-tab { 
    width: 100%; 
    border-collapse: collapse; 
    font-size: 6.2pt; 
    margin: 1.5px 0; 
    line-height: 1.1;
  }
  table.eea-tab th, table.eea-tab td { 
    border: 0.5px solid #94a3b8; 
    padding: 0.8px 1.5px; 
    text-align: center; 
  }
  table.eea-tab th { 
    background: #f8fafc; 
    font-weight: 700; 
  }
  ul { margin: 0; padding-left: 10px; }
  li { margin-bottom: 1px; }
  p { margin: 1px 0; }
}
@media screen {
  body { font-family: sans-serif; font-size: 11px; line-height: 1.4; padding: 15px; max-width: 1200px; margin: 0 auto; }
  .grid-3col { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 12px; }
  .box { border: 1px solid #cbd5e1; border-radius: 4px; padding: 8px; margin-bottom: 10px; }
  .box-title { font-weight: bold; background: #f1f5f9; padding: 4px; margin: -8px -8px 6px -8px; }
  table.eea-tab { width: 100%; border-collapse: collapse; margin: 6px 0; font-size: 10px; }
  table.eea-tab th, table.eea-tab td { border: 1px solid #cbd5e1; padding: 3px; text-align: center; }
  .formula { font-family: monospace; font-weight: bold; color: #1d4ed8; }
  .keyword { font-weight: bold; color: #b91c1c; }
  .step { font-weight: bold; color: #047857; }
}
</style>

# USTH CRYPTOGRAPHY - TỔNG HỢP CÔNG THỨC & PHƯƠNG PHÁP GIẢI TỰ LUẬN (CHEATSHEET A4)
<div class="meta-sub">Dành cho phòng thi | Quy chuẩn 100% công thức tổng quát & bước giải | Khuyết số cụ thể để tính qua Tool</div>

<div class="grid-3col">

<!-- ==================== CỘT 1: NỀN TẢNG TOÁN HỌC & CỔ ĐIỂN ==================== -->
<div class="col">

  <!-- BOX 1: EEA VÀ NGHỊCH ĐẢO MODULO -->
  <div class="box">
    <div class="box-title">1. TẠI SAO CẦN EEA & NGHỊCH ĐẢO MODULO?</div>
    <p><b>Bản chất:</b> Trong $\mathbb{Z}_m$, không có phép chia. Phép chia $b/a \pmod m$ thực chất là nhân $b \cdot a^{-1} \pmod m$.</p>
    <p><b>Định nghĩa:</b> $x = a^{-1} \pmod m \iff a \cdot x \equiv 1 \pmod m \iff a \cdot x - k \cdot m = 1$.</p>
    <p><b>Tại sao cần thuật toán Euclid mở rộng (EEA)?</b></p>
    <ul>
      <li>Đẳng thức Bézout khẳng định: Luôn tồn tại 2 số nguyên $s, t$ sao cho: <span class="formula">$\gcd(a, m) = a \cdot s + m \cdot t$</span>.</li>
      <li>Điều kiện tồn tại nghịch đảo: <span class="keyword">$\gcd(a, m) = 1$</span>.</li>
      <li>Khi đó: $a \cdot s + m \cdot t = 1 \implies a \cdot s \equiv 1 \pmod m \implies \mathbf{a^{-1} \equiv s \pmod m}$.</li>
      <li>Nếu $s < 0 \implies \mathbf{a^{-1} = s + m}$.</li>
    </ul>
    <p><b>Quy tắc lập bảng truy hồi EEA 5 cột:</b></p>
    <table class="eea-tab">
      <tr><th>Bước</th><th>q</th><th>r</th><th>s</th><th>t</th><th>Phương trình chia</th></tr>
      <tr><td>init</td><td>-</td><td>$r_0 = m$</td><td>$s_0 = 1$</td><td>$t_0 = 0$</td><td>Modulus $m$</td></tr>
      <tr><td>init</td><td>-</td><td>$r_1 = a$</td><td>$s_1 = 0$</td><td>$t_1 = 1$</td><td>Số cần nghịch đảo $a$</td></tr>
      <tr><td>$i$</td><td>$q_i$</td><td>$r_i$</td><td>$s_i$</td><td>$t_i$</td><td>$r_{i-2} = q_i \cdot r_{i-1} + r_i$</td></tr>
    </table>
    <p><b>Công thức truy hồi từng dòng:</b></p>
    <ul>
      <li>Thương số: <span class="formula">$q_i = \lfloor r_{i-2} / r_{i-1} \rfloor$</span> (chia lấy phần nguyên).</li>
      <li>Phần dư: <span class="formula">$r_i = r_{i-2} - q_i \cdot r_{i-1}$</span>.</li>
      <li>Hệ số $s$: <span class="formula">$s_i = s_{i-2} - q_i \cdot s_{i-1}$</span>.</li>
      <li>Hệ số $t$: <span class="formula">$t_i = t_{i-2} - q_i \cdot t_{i-1}$</span>.</li>
      <li><span class="step">Dừng lại:</span> Khi $r_i = 0$. Giá trị $r_{i-1} = \gcd(a, m) = 1$. Nghịch đảo là hệ số tương ứng ($s_{i-1}$ hoặc $t_{i-1}$).</li>
    </ul>
  </div>

  <!-- BOX 2: SQUARE AND MULTIPLY -->
  <div class="box">
    <div class="box-title">2. LŨY THỪA NHANH (SQUARE-AND-MULTIPLY)</div>
    <p><b>Bài toán:</b> Tính <span class="formula">$y = x^c \pmod n$</span> với số mũ $c$ rất lớn.</p>
    <p><b>Các bước thực hiện tự luận:</b></p>
    <ul>
      <li><span class="step">B1:</span> Đổi số mũ $c$ sang nhị phân: $c = (b_k b_{k-1} \dots b_1 b_0)_2$.</li>
      <li><span class="step">B2:</span> Đặt giá trị tích lũy $y = 1$.</li>
      <li><span class="step">B3:</span> Quét từng bit từ trái sang phải ($i = k$ về $0$):
        <br>• <b>Luôn luôn Bình phương:</b> <span class="formula">$y = y^2 \pmod n$</span> (Square).
        <br>• <b>Nếu bit $b_i = 1$:</b> Nhân thêm cơ số: <span class="formula">$y = (y \cdot x) \pmod n$</span> (Multiply).
      </li>
      <li>Kẻ bảng gồm các cột: <code>Bước | Bit | Phép toán | Công thức tính | Giá trị y</code>.</li>
    </ul>
  </div>

  <!-- BOX 3: MẬT MÃ CỔ ĐIỂN & ĐỒNG DƯ KHÁC -->
  <div class="box">
    <div class="box-title">3. MẬT MÃ CỔ ĐIỂN & ĐỒNG DƯ BẬC NHẤT</div>
    <ul>
      <li><b>Caesar:</b> Mã hóa $C = (P + k) \pmod{26}$ | Giải mã $P = (C - k) \pmod{26}$.</li>
      <li><b>Affine:</b> $C = (a \cdot P + b) \pmod{26}$ (ĐK: $\gcd(a, 26) = 1$).
        <br>Giải mã: <span class="formula">$P = a^{-1} \cdot (C - b) \pmod{26}$</span>.
      </li>
      <li><b>Vigenère:</b> $C_i = (P_i + K_{i \pmod m}) \pmod{26}$ | $P_i = (C_i - K_{i \pmod m}) \pmod{26}$.</li>
      <li><b>Vernam / One-Time Pad:</b> $C = P \oplus K$ | $P = C \oplus K$.</li>
      <li><b>Định lý số dư Trung Hoa (CRT):</b> Hệ $x \equiv a_i \pmod{m_i}$ với $\gcd(m_i, m_j) = 1$.
        <br>1. $M = \prod_{i=1}^n m_i$.
        <br>2. $M_i = M / m_i$ và tìm $y_i = M_i^{-1} \pmod{m_i}$ bằng EEA.
        <br>3. Nghiệm duy nhất: <span class="formula">$x = \left(\sum_{i=1}^n a_i \cdot M_i \cdot y_i\right) \pmod M$</span>.
      </li>
    </ul>
  </div>

</div>

<!-- ==================== CỘT 2: KHỐI DES, RSA VÀ PKI ==================== -->
<div class="col">

  <!-- BOX 4: DES S-BOX -->
  <div class="box">
    <div class="box-title">4. TRA CỨU HỘP S-BOX S1 TRONG DES</div>
    <p><b>Quy trình tự luận từng bước:</b></p>
    <ul>
      <li><span class="step">Bước 1:</span> Rút gọn số nguyên đầu vào: <span class="formula">$x = (\text{Student\_ID}) \pmod{64}$</span>.</li>
      <li><span class="step">Bước 2:</span> Biểu diễn $x$ dưới dạng nhị phân 6 bit:
        <br><span class="formula">$x = (b_1 b_2 b_3 b_4 b_5 b_6)_2$</span>.
      </li>
      <li><span class="step">Bước 3:</span> Xác định tọa độ Hàng và Cột:
        <br>• <b>Hàng (Row) $r$:</b> Ghép bit ngoài cùng: <span class="formula">$r = (b_1 b_6)_2 \in \{0, 1, 2, 3\}$</span>.
        <br>• <b>Cột (Col) $c$:</b> Ghép 4 bit ở giữa: <span class="formula">$c = (b_2 b_3 b_4 b_5)_2 \in \{0 \dots 15\}$</span>.
      </li>
      <li><span class="step">Bước 4:</span> Gióng hàng $r$ và cột $c$ trong ma trận $S_1$ cho trước:
        <br>$\implies \mathbf{\text{Out}} = S_1[r][c]$ (thập phân) $\implies$ đổi sang 4 bit nhị phân.
      </li>
      <li><b>Ý nghĩa lý thuyết:</b> S-Box là thành phần phi tuyến duy nhất trong DES, tạo hiệu ứng hỗn loạn (Confusion).</li>
    </ul>
  </div>

  <!-- BOX 5: HỆ MÃ HÓA RSA -->
  <div class="box">
    <div class="box-title">5. TẠO KHÓA, MÃ HÓA & GIẢI MÃ RSA</div>
    <p><b>Quy trình thiết lập khóa (Key Generation):</b></p>
    <ul>
      <li><span class="step">B1:</span> Chọn 2 số nguyên tố bí mật $p$ và $q$ ($p \ne q$).</li>
      <li><span class="step">B2:</span> Tính Modulus: <span class="formula">$N = p \cdot q$</span>.</li>
      <li><span class="step">B3:</span> Tính hàm phi Euler: <span class="formula">$\Phi(N) = (p - 1)(q - 1)$</span>.</li>
      <li><span class="step">B4:</span> Chọn số mũ công khai $e$ thỏa mãn:
        <br>• $1 < e < \Phi(N)$ và <span class="keyword">$\gcd(e, \Phi(N)) = 1$</span> (phân tích thừa số $\Phi(N)$ để chứng minh).
      </li>
      <li><span class="step">B5:</span> Tính số mũ bí mật $d$ bằng thuật toán EEA:
        <br><span class="formula">$d = e^{-1} \pmod{\Phi(N)} \iff e \cdot d \equiv 1 \pmod{\Phi(N)}$</span>.
      </li>
      <li><b>Cặp khóa:</b> Khóa công khai $k_{pub} = (N, e)$; Khóa bí mật $k_{pri} = (N, d)$.</li>
    </ul>
    <p><b>Quá trình Mã hóa & Giải mã:</b></p>
    <ul>
      <li><b>Mã hóa (Encryption):</b> Bản rõ $M < N \implies$ Bản mã: <span class="formula">$C = M^e \pmod N$</span>.</li>
      <li><b>Giải mã (Decryption):</b> Bản rõ khôi phục: <span class="formula">$M = C^d \pmod N$</span>.</li>
      <li><b>Chứng minh tính đúng đắn:</b> Dựa trên Định lý Euler ($M^{\Phi(N)} \equiv 1 \pmod N$):
        <br>$C^d \equiv (M^e)^d \equiv M^{ed} \equiv M^{k \cdot \Phi(N) + 1} \equiv (M^{\Phi(N)})^k \cdot M \equiv 1^k \cdot M \equiv M \pmod N$.
      </li>
    </ul>
  </div>

  <!-- BOX 6: CHỨNG CHỈ PKI & EMAIL HYBRID -->
  <div class="box">
    <div class="box-title">6. CHỨNG CHỈ SỐ PKI CA & EMAIL BẢO MẬT</div>
    <p><b>Chứng chỉ số RSA cấp bởi CA:</b></p>
    <ul>
      <li>CA có cặp khóa $(e_{CA}, d_{CA}, N_{CA})$.</li>
      <li><b>Cấp chứng chỉ:</b> CA ký số lên định danh/khóa $M$: <span class="formula">$S_{CA} = M^{d_{CA}} \pmod{N_{CA}}$</span>.</li>
      <li><b>Xác thực:</b> Người dùng kiểm tra: <span class="formula">$V = (S_{CA})^{e_{CA}} \pmod{N_{CA}}$</span>. Nếu $V == M \implies$ Hợp lệ!</li>
    </ul>
    <p><b>Quy trình gửi nhận Email bảo mật PKI (Hybrid):</b></p>
    <ul>
      <li><b>Bên gửi (Alice):</b>
        <br>1. Sinh khóa phiên đối xứng ngẫu nhiên $K_{sym}$ (AES/DES).
        <br>2. Mã hóa nội dung thư: $C = E_{K_{sym}}(\text{Email})$.
        <br>3. Mã hóa khóa phiên bằng khóa công khai Bob: $C_K = E_{e_B}(K_{sym})$.
        <br>4. Ký số lên băm thư bằng khóa bí mật Alice: $\sigma = S_{d_A}(\text{Hash}(\text{Email}))$.
        <br>5. Đóng gói gửi đi: $(C, C_K, \sigma, \text{Cert}_A)$.
      </li>
      <li><b>Bên nhận (Bob):</b>
        <br>1. Dùng khóa riêng $d_B$ giải mã $C_K \implies$ lấy lại $K_{sym}$.
        <br>2. Dùng $K_{sym}$ giải mã $C \implies$ lấy lại nội dung Email.
        <br>3. Dùng $e_A$ (từ $\text{Cert}_A$) xác thực chữ ký $\sigma \implies$ toàn vẹn & chống chối bỏ.
      </li>
    </ul>
  </div>

</div>

<!-- ==================== CỘT 3: CHỮ KÝ ELGAMAL, DHKE, SHA-1 ==================== -->
<div class="col">

  <!-- BOX 7: CHỮ KÝ ELGAMAL -->
  <div class="box">
    <div class="box-title">7. CHỮ KÝ SỐ ELGAMAL & CHỨNG CHỈ CA</div>
    <p><b>Tham số hệ thống:</b> Số nguyên tố $p$, phần tử sinh $\alpha \in \mathbb{Z}_p^*$.</p>
    <p><b>Tạo khóa:</b> Chọn khóa bí mật $d \in [2, p-2] \implies$ Khóa công khai: <span class="formula">$\beta = \alpha^d \pmod p$</span>.</p>
    <p><b>Quy trình Ký số thông điệp $x$ (hoặc $x_A = x + e_A$):</b></p>
    <ul>
      <li><span class="step">Bước 1 (Điều kiện tiên quyết):</span> Chọn khóa tạm thời (Ephemeral key) $k_E \in [1, p-2]$ sao cho: <span class="keyword">$\gcd(k_E, p-1) = 1$</span>.
        <br><i>Lưu ý quan trọng:</i> Nếu $\gcd(k_E, p-1) \ne 1 \implies$ <b>VÔ NGHIỆM</b> vì không tồn tại $k_E^{-1} \pmod{p-1}$!
      </li>
      <li><span class="step">Bước 2:</span> Tính thành phần chữ ký $r$:
        <br><span class="formula">$r = \alpha^{k_E} \pmod p$</span>.
      </li>
      <li><span class="step">Bước 3:</span> Tìm nghịch đảo modulo $p-1$:
        <br><span class="formula">$k_E^{-1} \pmod{p-1}$</span> (dùng thuật toán EEA với $p-1$).
      </li>
      <li><span class="step">Bước 4:</span> Tính thành phần chữ ký $s$:
        <br><span class="formula">$s = (x - d \cdot r) \cdot k_E^{-1} \pmod{p-1}$</span>.
        <br><i>Lưu ý số âm:</i> Nếu $(x - d \cdot r) < 0$, quy về phần dư dương bằng cách cộng thêm $p-1$: <span class="formula">$((x - dr) \pmod{p-1} + (p-1)) \pmod{p-1}$</span>.
      </li>
      <li>$\implies$ Cặp chữ ký số là $\mathbf{(r, s)}$. Chứng chỉ: $\text{Cert} = (x, (r, s))$.</li>
    </ul>
    <p><b>Quy trình Xác minh chữ ký (Verification):</b></p>
    <ul>
      <li>Người nhận có: $(p, \alpha, \beta)$, thông điệp $x$ và chữ ký $(r, s)$.</li>
      <li><span class="step">B1:</span> Tính <span class="formula">$v_1 = (\beta^r \cdot r^s) \pmod p = [(\beta^r \bmod p) \cdot (r^s \bmod p)] \pmod p$</span>.</li>
      <li><span class="step">B2:</span> Tính <span class="formula">$v_2 = \alpha^x \pmod p$</span>.</li>
      <li><span class="step">B3:</span> So sánh: Nếu <span class="keyword">$v_1 \equiv v_2 \pmod p$</span> $\implies$ Chữ ký hợp lệ!</li>
      <li><b>Chứng minh toán học:</b>
        <br>$\beta^r \cdot r^s \equiv (\alpha^d)^r \cdot (\alpha^{k_E})^s \equiv \alpha^{dr + k_E s} \pmod p$.
        <br>Vì $s \equiv (x - dr)k_E^{-1} \pmod{p-1} \implies k_E s \equiv x - dr \pmod{p-1}$.
        <br>$\implies dr + k_E s \equiv dr + x - dr \equiv x \pmod{p-1}$.
        <br>Theo định lý Fermat nhỏ: $\alpha^{dr + k_E s} \equiv \alpha^x \pmod p \implies v_1 = v_2$.
      </li>
    </ul>
  </div>

  <!-- BOX 8: DIFFIE-HELLMAN -->
  <div class="box">
    <div class="box-title">8. TRAO ĐỔI KHÓA DIFFIE-HELLMAN (DHKE)</div>
    <p><b>Thiết lập công khai:</b> Số nguyên tố lớn $p$, phần tử sinh $\alpha \in \mathbb{Z}_p^*$.</p>
    <p><b>Giao thức chuẩn:</b></p>
    <ul>
      <li>Alice chọn bí mật $a \in [2, p-2] \implies$ gửi Bob: <span class="formula">$k_A = \alpha^a \pmod p$</span>.</li>
      <li>Bob chọn bí mật $b \in [2, p-2] \implies$ gửi Alice: <span class="formula">$k_B = \alpha^b \pmod p$</span>.</li>
      <li><b>Tính Khóa phiên chung (Shared Session Key):</b>
        <br>• Alice tính: <span class="formula">$k_{AB} = (k_B)^a \pmod p$</span>.
        <br>• Bob tính: <span class="formula">$k_{AB} = (k_A)^b \pmod p$</span>.
        <br>$\implies k_{AB} = (\alpha^b)^a = (\alpha^a)^b = \mathbf{\alpha^{a \cdot b} \pmod p}$.
      </li>
    </ul>
    <p><b>Tấn công Kẻ-đứng-giữa (Man-in-the-Middle - MITM):</b></p>
    <ul>
      <li>Oscar đứng giữa chặn $k_A, k_B$. Oscar tự sinh số bí mật $o$, tính $k_O = \alpha^o \pmod p$ và gửi $k_O$ cho cả Alice và Bob.</li>
      <li>Khóa phiên Alice - Oscar: <span class="formula">$k_{AO} = (k_O)^a = (k_A)^o \pmod p$</span>.</li>
      <li>Khóa phiên Bob - Oscar: <span class="formula">$k_{BO} = (k_O)^b = (k_B)^o \pmod p$</span>.</li>
      <li>Oscar có thể giải mã, đọc trộm và sửa đổi toàn bộ thông điệp.</li>
      <li><b>Khắc phục:</b> Ký số lên khóa công khai hoặc dùng chứng chỉ số CA.</li>
    </ul>
  </div>

  <!-- BOX 9: SHA-1 VÀ HÀM BĂM -->
  <div class="box">
    <div class="box-title">9. ĐỆM SHA-1 (PADDING) & HÀM BĂM KHỐI</div>
    <p><b>Quy trình đệm SHA-1 cho thông điệp dài $l$ bit:</b></p>
    <ul>
      <li><span class="step">Bước 1:</span> Nối 1 bit '1' vào cuối thông điệp $M$ (độ dài thành $l + 1$).</li>
      <li><span class="step">Bước 2:</span> Thêm $k$ bit '0' sao cho: <span class="formula">$(l + 1 + k) \equiv 448 \pmod{512}$</span>
        <br>$\implies \mathbf{k = (447 - (l \bmod 512)) \bmod 512}$ (với $0 \le k < 512$).
        <br><i>Ví dụ tính nhanh $k$:</i> Lấy $l \pmod{512} = \text{rem}$. Nếu $\text{rem} \le 447 \implies k = 447 - \text{rem}$. Nếu $\text{rem} > 447 \implies k = 447 - \text{rem} + 512$.
      </li>
      <li><span class="step">Bước 3:</span> Nối thêm <b>64 bit</b> biểu diễn nhị phân của chiều dài ban đầu $l$ (Big-Endian).</li>
      <li><span class="step">Bước 4:</span> Tổng số bit sau đệm: <span class="formula">$L = l + 1 + k + 64$</span> bits.
        <br>Số khối 512-bit: <span class="formula">$N = L / 512$</span> (luôn là số nguyên).
      </li>
    </ul>
    <p><b>Sơ đồ nén Davies-Meyer:</b> Khối băm xây dựng từ mã hóa khối:
      <br><span class="formula">$h_i = E_{m_i}(h_{i-1}) \oplus h_{i-1}$</span> (Khối tin $m_i$ làm Khóa, $h_{i-1}$ làm Bản rõ).
    </p>
    <p><b>Độ an toàn va chạm (Birthday Paradox):</b>
      <br>Hàm băm đầu ra $n$ bit có độ phức tạp tìm va chạm (Collision resistance) là <span class="keyword">$\mathcal{O}(2^{n/2})$</span> thay vì $2^n$.
      <br>Xác suất va chạm đạt $50\%$ khi số lượng thông điệp băm thử nghiệm đạt: <span class="formula">$k \approx 1.177 \cdot \sqrt{2^n} = 1.177 \cdot 2^{n/2}$</span>.
    </p>
  </div>

</div>

</div>
