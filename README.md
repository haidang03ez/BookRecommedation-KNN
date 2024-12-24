Lý do sử dụng cosine trong KNN 
1. Tập trung vào hướng (góc) của véc-tơ thay vì độ lớn
•	Độ tương đồng Cosine đo lường góc giữa hai véc-tơ thay vì độ lớn của chúng. Điều này quan trọng trong các bài toán mà mối quan hệ tương đối (cấu trúc) giữa các thuộc tính quan trọng hơn tổng giá trị.
•	Ví dụ:
o	Trong bài toán gợi ý sách, nếu một người dùng đánh giá sách theo thang điểm khác nhau (1-5 hoặc 0-10), thì Cosine Similarity sẽ tập trung vào mẫu hình (pattern) đánh giá thay vì giá trị tuyệt đối.
________________________________________
2. Khả năng xử lý dữ liệu thưa (sparse data)
•	Dữ liệu trong các bài toán như hệ thống gợi ý thường rất thưa (nhiều giá trị 0 hoặc NaN).
•	Độ tương đồng Cosine vẫn hoạt động tốt với ma trận thưa vì nó chỉ so sánh các thuộc tính chung giữa hai véc-tơ, bỏ qua các mục mà cả hai đều không có giá trị.
________________________________________
3. Không bị ảnh hưởng bởi độ lớn tuyệt đối
•	Khoảng cách Euclid bị ảnh hưởng bởi độ lớn của véc-tơ. Nếu một người dùng đánh giá cao tất cả các sách và người khác đánh giá thấp tất cả các sách nhưng theo cùng một mẫu hình, Cosine sẽ nhận ra sự tương đồng của họ, trong khi Euclid có thể không.
________________________________________
4. Hiệu quả tính toán
•	Trong không gian véc-tơ, độ tương đồng Cosine được tính nhanh chóng và hiệu quả, đặc biệt khi sử dụng thư viện tối ưu hóa như NumPy hoặc Scikit-learn.
________________________________________
5. Ứng dụng trong KNN
•	Khi sử dụng KNN, việc xác định các "hàng xóm gần nhất" dựa trên độ tương đồng Cosine phù hợp hơn trong các bài toán có dữ liệu dạng véc-tơ (ví dụ: biểu diễn người dùng/sách dưới dạng đặc trưng).
•	Điều này giúp mô hình tập trung vào mối quan hệ giữa các đặc trưng thay vì phụ thuộc vào khoảng cách vật lý.
________________________________________
Khi nào nên dùng Cosine Similarity?
•	Dữ liệu có tính chất véc-tơ.
•	Dữ liệu thưa và có thang đo khác nhau giữa các đối tượng.
•	Khi muốn tập trung vào mối quan hệ tương đối giữa các thuộc tính thay vì giá trị tuyệt đối.
Nếu ông cần thêm ví dụ minh họa, con có thể triển khai chi tiết hơn!
Lý do sử dụng pivot table trong KNN
Pivot table chuyển đổi dữ liệu gọn gàng (tidy data) thành ma trận, trong đó:
•	Hàng: Biểu thị các đối tượng (ví dụ: sách).
•	Cột: Biểu thị các đặc điểm hoặc người dùng.
•	Giá trị: Biểu thị mối quan hệ (ví dụ: đánh giá sách).
Lợi ích khi sử dụng pivot table:
-	Chuẩn hóa dữ liệu thành ma trận:
o	KNN yêu cầu đầu vào là dữ liệu dạng vector để tính khoảng cách hoặc độ tương đồng. 
o	Pivot table chuyển đổi dữ liệu phân tán thành ma trận sẵn sàng cho các phép toán.
-	Tính toán dễ dàng: Với pivot table, các công thức tính toán (như cosine similarity hoặc khoảng cách Euclidean) được áp dụng trực tiếp trên các cột hoặc hàng.
-	Xử lý dữ liệu thưa (sparse data): Pivot table giúp tổ chức dữ liệu sao cho các giá trị trống (NaN) có thể được xử lý (bằng cách điền giá trị trung bình hoặc bỏ qua).
-	Tương thích với các phương pháp học máy: Ma trận từ pivot table là đầu vào chuẩn cho các thuật toán như KNN, PCA, hoặc clustering.
Pivot table là bước chuyển đổi dữ liệu cần thiết để áp dụng KNN và các phương pháp tính toán tương đồng.
Theo hình học, pivot table tạo ra không gian vector, trong đó khoảng cách và góc giữa các vector được sử dụng để xác định mối quan hệ giữa người dùng và sách.
Liên hệ giữa pivot table và Cosine
-	Pivot Table và Không Gian Vector
•	Pivot table chuyển đổi dữ liệu thành một ma trận n chiều:
o	Hàng: Đại diện cho các đối tượng (ví dụ: sách hoặc người dùng).
o	Cột: Biểu thị các đặc điểm (ví dụ: người dùng hoặc sách).
o	Giá trị: Là số liệu cụ thể (ví dụ: điểm đánh giá).
•	Sau khi pivot, mỗi hàng hoặc cột trở thành một vector trong không gian n chiều.
Ví dụ:
o	Mỗi người dùng là một vector trong không gian với mỗi chiều đại diện cho một sách.
o	Hoặc mỗi sách là một vector trong không gian với mỗi chiều đại diện cho một người dùng.
________________________________________
-	Cosine Similarity và Vector
•	Cosine similarity đo lường độ tương đồng giữa hai vector (ví dụ: hai người dùng hoặc hai sách) bằng cách tính cosine của góc giữa chúng.
o	Giá trị cosine càng lớn (gần 1), các vector càng cùng hướng (tương tự nhau).
o	Giá trị cosine càng nhỏ (gần -1 hoặc 0), các vector càng khác hướng (ít tương tự).
•	Pivot table cung cấp cơ sở để cosine similarity hoạt động, vì nó:
o	Tạo các vector từ dữ liệu thô.
o	Bố trí dữ liệu dưới dạng có thể so sánh bằng cách tính góc giữa các vector.
________________________________________
-	Mối Liên Hệ
1.	Dữ liệu từ pivot table:
o	Pivot table định hình dữ liệu sao cho mỗi đối tượng (người dùng hoặc sách) trở thành một vector.
o	Điều này cho phép cosine similarity hoạt động, vì nó yêu cầu vector đầu vào.
2.	Cosine dựa trên cấu trúc ma trận pivot:
o	Người dùng: Tương đồng dựa trên điểm đánh giá các sách.
	Vector người dùng: Cột trong pivot table (đánh giá của một người dùng với các sách).
o	Sách: Tương đồng dựa trên sự đánh giá từ các người dùng.
	Vector sách: Hàng trong pivot table (điểm đánh giá từ các người dùng cho một sách).
3.	Pivot giúp xử lý dữ liệu thưa (sparse data):
o	Pivot table có thể chứa nhiều giá trị trống (NaN), đặc biệt là khi không phải mọi người dùng đều đánh giá tất cả sách.
o	Điều này được xử lý (bằng cách điền giá trị mặc định hoặc loại bỏ), sau đó cosine similarity được áp dụng.
________________________________________
-	Minh Họa
•	Pivot table giống như một không gian vector:
o	Hàng hoặc cột là các vector.
o	Cosine similarity đo lường góc giữa các vector này, dựa trên dữ liệu trong pivot.
Ví dụ:
o	Vector User 1: [5, 4, NaN].
o	Vector User 2: [NaN, 2, 1].
o	Cosine similarity đo góc giữa các vector này, phản ánh độ tương đồng giữa người dùng dựa trên đánh giá sách.
________________________________________
-	Kết Luận
Pivot table là tiền đề để cosine similarity hoạt động:
•	Nó tạo ra các vector từ dữ liệu thô.
•	Dựa vào pivot, cosine similarity xác định mức độ tương đồng giữa các đối tượng (người dùng hoặc sách), giúp hệ thống gợi ý vận hành hiệu quả.
