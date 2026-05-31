# Input:
# - menu_choice: lựa chọn chức năng từ 1-5
# - product_id: mã sản phẩm (str)
# - buy_quantity: số lượng khách mua (int)
# - import_quantity: số lượng nhập kho (int)

# Output:
# - Danh sách sản phẩm và trạng thái tồn kho
# - Thông tin bán hàng thành công
# - Thông tin nhập kho thành công
# - Báo cáo doanh thu cửa hàng
# - Các thông báo lỗi khi dữ liệu không hợp lệ

# Giải pháp:
# - Dùng list chứa các dictionary để lưu thông tin sản phẩm
# - Dùng strip() và upper() để chuẩn hóa mã sản phẩm
# - Dùng isdigit() để kiểm tra dữ liệu số
# - Cập nhật tồn kho và số lượng đã bán trực tiếp trên dictionary
# - Dùng vòng lặp để tìm sản phẩm theo mã
# - Tính doanh thu bằng công thức: price * sold
# - Tìm sản phẩm bán chạy nhất bằng cách so sánh sold

# Thuật toán:
# - Hiển thị menu chính
# - Người dùng chọn chức năng
# - Hiển thị sản phẩm và trạng thái tồn kho
# - Bán hàng và cập nhật dữ liệu
# - Nhập thêm hàng vào kho
# - Thống kê doanh thu và sản phẩm bán chạy
# - Thoát chương trình khi chọn 5

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:
    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")

    menu_choice = input("Nhập lựa chọn của bạn: ").strip()

    if menu_choice == "1":
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("\nDanh sách sản phẩm hiện tại:")

            for index, product in enumerate(product_list, start=1):
                quantity = product["quantity"]

                if quantity == 0:
                    status = "Hết hàng"
                elif quantity <= 5:
                    status = "Sắp hết hàng"
                else:
                    status = "Còn hàng"

                print(
                    f"{index}. Mã SP: {product['product_id']} | "
                    f"Tên: {product['product_name']} | "
                    f"Giá: {product['price']} | "
                    f"Tồn kho: {product['quantity']} | "
                    f"Đã bán: {product['sold']} | "
                    f"Trạng thái: {status}"
                )

    elif menu_choice == "2":
        product_id = input(
            "Nhập mã sản phẩm khách muốn mua: "
        ).strip().upper()

        found = False

        for product in product_list:
            if product["product_id"] == product_id:
                found = True

                buy_quantity = input(
                    "Nhập số lượng khách mua: "
                ).strip()

                if (
                    not buy_quantity.isdigit()
                    or int(buy_quantity) <= 0
                ):
                    print("Số lượng mua không hợp lệ")
                    break

                buy_quantity = int(buy_quantity)

                if buy_quantity > product["quantity"]:
                    print("Số lượng trong kho không đủ để bán")
                    break

                product["quantity"] -= buy_quantity
                product["sold"] += buy_quantity

                payment = buy_quantity * product["price"]

                print("Bán hàng thành công")
                print(f"Số tiền khách cần thanh toán: {payment:,} VNĐ")
                break

        if not found:
            print("Không tìm thấy sản phẩm cần bán")

    elif menu_choice == "3":
        product_id = input(
            "Nhập mã sản phẩm cần nhập thêm: "
        ).strip().upper()

        found = False

        for product in product_list:
            if product["product_id"] == product_id:
                found = True

                import_quantity = input(
                    "Nhập số lượng nhập thêm: "
                ).strip()

                if (
                    not import_quantity.isdigit()
                    or int(import_quantity) <= 0
                ):
                    print("Số lượng nhập kho không hợp lệ")
                    break

                import_quantity = int(import_quantity)

                product["quantity"] += import_quantity

                print("Nhập kho thành công")
                break

        if not found:
            print("Không tìm thấy sản phẩm cần nhập kho")

    elif menu_choice == "4":
        total_revenue = 0
        best_seller = None
        max_sold = 0

        sold_exist = False

        for product in product_list:
            if product["sold"] > 0:
                sold_exist = True
                break

        if not sold_exist:
            print("Chưa có doanh thu phát sinh.")
        else:
            print("\n===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")

            for index, product in enumerate(product_list, start=1):
                revenue = product["price"] * product["sold"]

                total_revenue += revenue

                if product["sold"] > max_sold:
                    max_sold = product["sold"]
                    best_seller = product["product_name"]

                print(
                    f"{index}. {product['product_name']} | "
                    f"Đã bán: {product['sold']} | "
                    f"Doanh thu: {revenue}"
                )

            print(f"\nTổng doanh thu: {total_revenue}")
            print(f"Sản phẩm bán chạy nhất: {best_seller}")

    elif menu_choice == "5":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")