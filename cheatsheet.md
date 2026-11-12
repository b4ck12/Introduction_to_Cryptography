<style>
@page {
  size: A4 portrait;
  margin: 6mm 8mm 6mm 8mm;
}
@media print {
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 8pt;
    line-height: 1.22;
    color: #111;
    background: #fff;
    margin: 0;
    padding: 0;
  }
  h1 { font-size: 11pt; margin: 0 0 2px 0; text-align: center; font-weight: 800; color: #1e3a8a; text-transform: uppercase; border-bottom: 1.5px solid #1e3a8a; padding-bottom: 2px; }
  .meta-bar { font-size: 7.5pt; text-align: center; margin-bottom: 4px; font-weight: 600; color: #475569; }
  .grid-2col { display: grid; grid-template-columns: 1fr 1fr; column-gap: 6mm; row-gap: 3mm; }
  .box { border: 1px solid #94a3b8; border-radius: 3px; padding: 3px 5px; background: #fff; break-inside: avoid; }
  .box-title { font-size: 8.5pt; font-weight: 700; color: #0f172a; background: #f1f5f9; margin: -3px -5px 3px -5px; padding: 2px 5px; border-bottom: 1px solid #cbd5e1; display: flex; justify-content: space-between; }
  table.compact-tab { width: 100%; border-collapse: collapse; font-size: 7.2pt; margin: 2px 0; }
  table.compact-tab th, table.compact-tab td { border: 0.5px solid #cbd5e1; padding: 1px 3px; text-align: center; }
  table.compact-tab th { background: #f8fafc; font-weight: 700; color: #334155; }
  .formula { font-family: "Courier New", monospace; font-weight: 700; color: #1d4ed8; font-size: 7.8pt; }
  .val { font-weight: 700; color: #b91c1c; }
  .step-num { font-weight: 700; color: #047857; }
  ul { margin: 1px 0; padding-left: 12px; }
  li { margin-bottom: 1px; }
}
</style>

# USTH CRYPTOGRAPHY - BẢNG CÔNG THỨC & DẠNG BÀI THI CUỐI KỲ (A4 CHEATSHEET)
<div class="meta-bar">Học phần: ICT3.001 / ICT3.08E | Dành cho phòng thi | SV: 23BA14056 (x = a = M = 56) | Tra soát siêu tốc</div>

<div class="grid-2col">

<!-- CỘT TRÁI -->
<div class="col-left">

  <!-- DẠNG 1 -->
  <div class="box">
    <div class="box-title"><span>1. TRA CỨU HỘP S-BOX DES S1 (3 ĐIỂM)</span> <span>Đề 2025, 2023</span></div>
    <ul>
      <li><b>B1 (Rút gọn ID):</b> $x = \text{Mã\_SV} \pmod{64}$. Với SV 056: $x = 56 \pmod{64} = \mathbf{56}$.</li>
      <li><b>B2 (Đổi 6 bit nhị phân):</b> $56_{10} = \mathbf{(111000)_2} \to (b_1 b_2 b_3 b_4 b_5 b_6)$.</li>
      <li><b>B3 (Xác định Hàng / Cột):</b>
        <br>• Hàng $r = (b_1 b_6)_2 = (10)_2 = \mathbf{2}$ (Dòng thứ 3: 0, 1, <b>2</b>, 3).
        <br>• Cột $c = (b_2 b_3 b_4 b_5)_2 = (1100)_2 = \mathbf{12}$ (Cột thứ 13: 0..15).
      </li>
      <li><b>B4 (Tra bảng $S_1$ tại Hàng 2, Cột 12):</b>
        <br>Hàng 2: `[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7,` <span class="val">3</span> `, 10, 5, 0]`
        <br>$\implies \mathbf{S_1(56) = 3 = (0011)_2}$ (Số lẻ $\to$ Chọn Question Set 01 đề 2023).
      </li>
    </ul>
  </div>

  <!-- DẠNG 2 -->
  <div class="box">
    <div class="box-title"><span>2. THIẾT LẬP KHÓA RSA & EUCLID MỞ RỘNG (EEA)</span> <span>Đề 2025, 2024</span></div>
    <ul>
      <li><b>B1 (Tính N và $\Phi(N)$):</b> $N = p \cdot q$ ; $\Phi(N) = (p-1)(q-1)$.
        <br><i>Đề 2025:</i> $p=139, q=227 \implies N = \mathbf{31553}, \Phi(N) = 138 \times 226 = \mathbf{31188}$.
      </li>
      <li><b>B2 (Chọn e nguyên tố cùng nhau với $\Phi(N)$):</b> Điều kiện $\gcd(e, \Phi(N)) = 1$.
        <br>Phân tích $\Phi(N) = 31188 = 2^2 \times 3 \times 7 \times 371 \implies$ chọn $e = \mathbf{125}$ (vì $125 = 5^3$).
      </li>
      <li><b>B3 (Tìm khóa riêng $d = e^{-1} \pmod{\Phi(N)}$ qua bảng EEA):</b>
        <table class="compact-tab">
          <tr><th>Bước</th><th>q</th><th>r</th><th>s</th><th>t</th><th>Phương trình chia</th></tr>
          <tr><td>init</td><td>-</td><td>31188</td><td>1</td><td>0</td><td>$r_0 = 31188$</td></tr>
          <tr><td>init</td><td>-</td><td>125</td><td>0</td><td>1</td><td>$r_1 = 125$</td></tr>
          <tr><td>1</td><td>249</td><td>63</td><td>1</td><td>-249</td><td>$31188 = 249 \times 125 + 63$</td></tr>
          <tr><td>2</td><td>1</td><td>62</td><td>-1</td><td>250</td><td>$125 = 1 \times 63 + 62$</td></tr>
          <tr><td>3</td><td>1</td><td>1</td><td>2</td><td>-499</td><td>$63 = 1 \times 62 + 1$</td></tr>
          <tr><td>4</td><td>62</td><td>0</td><td>-125</td><td>31188</td><td>$62 = 62 \times 1 + 0$</td></tr>
        </table>
        $d = t \pmod{\Phi(N)} = -499 \pmod{31188} = 31188 - 499 = \mathbf{30689}$.
        <br>• Cặp khóa: Khóa công khai $k_{pub} = (31553, 125)$; Khóa bí mật $k_{pri} = (31553, 30689)$.
      </li>
    </ul>
  </div>

  <!-- DẠNG 3 -->
  <div class="box">
    <div class="box-title"><span>3. MÃ HÓA & GIẢI MÃ RSA (SQUARE-AND-MULTIPLY)</span> <span>Đề 2025</span></div>
    <ul>
      <li><b>Công thức:</b> Mã hóa: $C = M^e \pmod N$ | Giải mã: $M = C^d \pmod N$.</li>
      <li><b>Thuật toán Nhân-Bình-Phương (Square-and-Multiply):</b>
        <br>1. Đổi số mũ $e$ sang nhị phân: $e = (b_k b_{k-1} \dots b_0)_2$.
        <br>2. Khởi tạo $y = 1$. Với mỗi bit từ trái sang phải:
        <br>&nbsp;&nbsp;&nbsp;&nbsp;• Luôn luôn tính: <span class="formula">Square: $y = y^2 \pmod N$</span>.
        <br>&nbsp;&nbsp;&nbsp;&nbsp;• Nếu bit = '1': <span class="formula">Multiply: $y = y \cdot M \pmod N$</span>.
      </li>
      <li><b>Đáp số đề 2025:</b>
        <br>• TH 1 ($M = 56$): $C = 56^{125} \pmod{31553} = \mathbf{2365}$ | Giải mã: $2365^{30689} = \mathbf{56}$.
        <br>• TH 2 ($M = 20260$): $C = 20260^{125} \pmod{31553} = \mathbf{24373}$ | Giải mã: $\mathbf{20260}$.
      </li>
    </ul>
  </div>

</div>

<!-- CỘT PHẢI -->
<div class="col-right">

  <!-- DẠNG 4 -->
  <div class="box">
    <div class="box-title"><span>4. CHỮ KÝ SỐ ELGAMAL & CHỨNG CHỈ SỐ CA</span> <span>Đề 2025, 2023</span></div>
    <ul>
      <li><b>Tham số CA:</b> Nguyên tố $p$, phần tử sinh $\alpha$, khóa bí mật $d \implies \beta = \alpha^d \pmod p$.</li>
      <li><b>B1 (Kiểm tra $k_E$):</b> Tiên quyết <span class="formula">$\gcd(k_E, p-1) = 1$</span>.
        <br><i>Bẫy đề thi:</i> Nếu đề ghi nhầm $k_E = 105 \implies \gcd(105, 996) = 3 \ne 1 \to$ Vô nghiệm!
        <br><i>Số chuẩn:</i> $k_E = 185 \implies \gcd(185, 996) = 1$ (Hợp lệ).
      </li>
      <li><b>B2 (Tính chữ ký $(r, s)$):</b>
        <br>1. <span class="formula">$r = \alpha^{k_E} \pmod p$</span>. (Đề 2025: $6^{185} \pmod{997} = \mathbf{591}$).
        <br>2. Tìm nghịch đảo: <span class="formula">$k_E^{-1} \pmod{p-1}$</span> qua EEA. ($185^{-1} \pmod{996} = \mathbf{533}$).
        <br>3. <span class="formula">$s = (x - d \cdot r) \cdot k_E^{-1} \pmod{p-1}$</span>.
        <br>&nbsp;&nbsp;&nbsp;Với $x = x_A = 56 + 125 = 181$:
        <br>&nbsp;&nbsp;&nbsp;$x - d \cdot r = 181 - 25 \times 591 = -14594 \equiv 346 \pmod{996}$.
        <br>&nbsp;&nbsp;&nbsp;$s = 346 \times 533 \pmod{996} = 184418 \pmod{996} = \mathbf{158}$.
        <br>$\implies$ Chữ ký $S = (r=591, s=158)$; Chứng chỉ $\text{Cert}_A = (x=181, (591, 158))$.
      </li>
      <li><b>B3 (Xác thực chữ ký):</b> Kiểm tra <span class="formula">$v_1 \equiv v_2 \pmod p$</span>:
        <br>$v_1 = \beta^r \cdot r^s \pmod p = 333^{591} \times 591^{158} \pmod{997} = 991 \times 985 \pmod{997} = \mathbf{72}$.
        <br>$v_2 = \alpha^x \pmod p = 6^{181} \pmod{997} = \mathbf{72}$. Vì $v_1 = v_2 = 72 \implies$ Hợp lệ!
      </li>
    </ul>
  </div>

  <!-- DẠNG 5 -->
  <div class="box">
    <div class="box-title"><span>5. GIAO THỨC TRAO ĐỔI KHÓA DIFFIE-HELLMAN</span> <span>Đề 2025, 2023</span></div>
    <ul>
      <li><b>Công khai:</b> Số nguyên tố lớn $p$, phần tử sinh $\alpha \in \mathbb{Z}_p^*$.</li>
      <li><b>Alice & Bob tính khóa công khai:</b>
        <br>• Alice chọn bí mật $a \implies k_A = \alpha^a \pmod p$.
        <br>• Bob chọn bí mật $b \implies k_B = \alpha^b \pmod p$.
      </li>
      <li><b>Tính Khóa phiên chung (Shared Session Key):</b>
        <br><span class="formula">$k_{AB} = (k_B)^a \pmod p = (k_A)^b \pmod p = \alpha^{a \cdot b} \pmod p$</span>.
      </li>
      <li><b>Đáp số đề 2025 ($p = 27361, \alpha = 6$):</b>
        <br>• Chuẩn đề in ($a = M = 20260, b = C = 24373$):
        <br>&nbsp;&nbsp;&nbsp;$k_A = 6^{20260} \equiv \mathbf{12} \pmod p$ ; $k_B = 6^{24373} \equiv \mathbf{3268} \pmod p$.
        <br>&nbsp;&nbsp;&nbsp;Khóa chung: $k_{AB} = 3268^{20260} = 12^{24373} \equiv \mathbf{20184} \pmod{27361}$.
        <br>• Biến thể dự phòng ($a = 56, b = 2365$): $k_{AB} = 26500^{56} \equiv \mathbf{17498}$.
      </li>
      <li><b>Tấn công MITM (Oscar đứng giữa):</b>
        <br>Oscar chọn bí mật $o$. Gửi $k_O = \alpha^o \pmod p$ cho cả Alice và Bob.
        <br>$\implies k_{AO} = (k_A)^o = (k_O)^a \pmod p$ | $k_{BO} = (k_B)^o = (k_O)^b \pmod p$.
      </li>
    </ul>
  </div>

  <!-- DẠNG 6 -->
  <div class="box">
    <div class="box-title"><span>6. TIỀN XỬ LÝ ĐỆM SHA-1 (PADDING) & HÀM BĂM</span> <span>Đề 2025, 2023</span></div>
    <ul>
      <li><b>Quy tắc đệm SHA-1 (Độ dài thông điệp $l$ bits):</b>
        <br>1. Nối <b>1 bit '1'</b> vào cuối thông điệp $M$.
        <br>2. Thêm <b>$k$ bit '0'</b> sao cho: <span class="formula">$(l + 1 + k) \equiv 448 \pmod{512}$</span>
        <br>&nbsp;&nbsp;&nbsp;$\implies k = (447 - (l \pmod{512})) \pmod{512}$ (với $0 \le k < 512$).
        <br>3. Thêm <b>64 bit</b> biểu diễn nhị phân của chiều dài ban đầu $l$.
        <br>$\implies$ Tổng số bit sau đệm: $L = l + 1 + k + 64$. Số khối 512-bit: $N = L / 512$.
      </li>
      <li><b>Tính toán nhanh:</b>
        <br>• Với $l = 20260$ bits: $20260 \pmod{512} = 292 \implies k = 447 - 292 = \mathbf{155}$ bits '0'.
        <br>&nbsp;&nbsp;&nbsp;Tổng bit $L = 20260 + 1 + 155 + 64 = 20480$ bits $\implies N = 20480 / 512 = \mathbf{40}$ khối.
        <br>• Với $l = 56$ bits: $56 \pmod{512} = 56 \implies k = 447 - 56 = \mathbf{391}$ bits '0' ($N = \mathbf{1}$ khối).
      </li>
      <li><b>Hàm băm khối Davies-Meyer:</b> $h_i = E_{m_i}(h_{i-1}) \oplus h_{i-1}$. Khối thông điệp $m_i$ đóng vai trò là KHÓA, digest trước $h_{i-1}$ là ĐẦU VÀO bản rõ.</li>
    </ul>
  </div>

  <!-- BẢNG BỎ TÚI CỰC NHANH -->
  <div class="box" style="border: 1.5px solid #1e3a8a; background: #f8fafc;">
    <div class="box-title" style="background: #e0e7ff; color: #1e3a8a;"><span>BẢNG TRA CỨU ĐÁP SỐ MÃ SV 23BA14056 (x = 56)</span> <span>QUAN TRỌNG</span></div>
    <table class="compact-tab" style="font-size: 7pt; margin: 1px 0;">
      <tr style="background:#e2e8f0;"><th>Phép tính</th><th>Đáp số</th><th>Ý nghĩa trong đề thi</th></tr>
      <tr><td>$56 \pmod{64}$</td><td><b>56</b></td><td>Đầu vào hộp DES S1: $56 = (111000)_2 \to$ Hàng 2, Cột 12 $\to$ <b>Output = 3</b></td></tr>
      <tr><td>$56 \pmod{26}$</td><td><b>4</b></td><td>Khóa Caesar $k = 4$, ký tự 'E'</td></tr>
      <tr><td>$\Phi(31553)$</td><td><b>31188</b></td><td>$\Phi(N)$ của RSA 2025 ($p=139, q=227$). Khóa $d = 125^{-1} \equiv \mathbf{30689}$</td></tr>
      <tr><td>RSA Encrypt</td><td><b>24373</b></td><td>Mã hóa đề in: $20260^{125} \pmod{31553} = 24373$. (Với $M=56 \to C = 2365$)</td></tr>
      <tr><td>ElGamal Sign</td><td><b>(591, 158)</b></td><td>Chữ ký đề 2025 với $k_E = 185, x_A = 181, d=25$. Xác minh: $v_1 = v_2 = \mathbf{72}$</td></tr>
      <tr><td>DHKE Key</td><td><b>20184</b></td><td>Khóa phiên đề in 2025 ($p=27361, \alpha=6, a=20260, b=24373$)</td></tr>
    </table>
  </div>

</div>

</div>
