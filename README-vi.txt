# PythonMixer
# Script Ghi Âm và Phát Lại Âm Thanh

## 1. Đó là gì?

Script nhỏ này có một mục tiêu duy nhất: ghi âm từ các thiết bị đầu vào (như micro máy tính xách tay của bạn, tai nghe, tai nghe hoặc tai nghe đặc biệt) và phát lại trên các thiết bị đầu ra (bao gồm loa máy tính xách tay của bạn, loa ngoại, TV, ampli hoặc tai nghe, tất cả đều kết nối với máy tính của bạn.

## 2. Được sử dụng để làm gì?

Script này có ích trong hai tình huống chính:

- **Giảng dạy:** Tại một số lớp học, có máy chiếu, nhưng không có micro. Nếu giọng nói của bạn quá yếu, Script này sẽ giúp bạn. Kết nối tai nghe qua Bluetooth, và giọng nói của bạn sẽ được truyền qua loa hoặc máy chiếu, đi kèm với bài thuyết trình của bạn.

- **Karaoke:** Đối với những người yêu ca hát nhưng không có hệ thống karaoke riêng, đơn giản là cắm máy tính xách tay của bạn vào TV, chọn bài hát karaoke yêu thích trên YouTube và hát thoải mái.

## 3. Cài đặt

Xin lưu ý rằng mặc dù Script này được thiết kế để hoạt động trên nhiều nền tảng khác nhau (Mac OSX, Linux và Windows), nó đã được thử nghiệm chủ yếu trên MacOSX.

Trước khi bạn có thể sử dụng Script, bạn cần cài đặt thêm hai thư viện. Mở cửa sổ terminal và chạy các lệnh sau:

```bash
$ pip install sounddevice
$ pip install numpy
```

## 4. Sử dụng

Sau khi bạn đã cài đặt các phụ thuộc cần thiết, bạn có thể bắt đầu sử dụng Script:

```bash
$ python3 main.py
```

Khi chạy Script, bạn sẽ được yêu cầu chọn cả thiết bị đầu vào (micro) và đầu ra (loa) từ danh sách các thiết bị có sẵn trên máy tính của bạn. Đảm bảo các thiết bị bạn muốn sử dụng đã được kết nối với máy tính trước khi chạy Script.

Dưới đây là giao diện lựa chọn:

```
AVAILABLE INPUT DEVICES:
====================
  0 LC34G55T, Core Audio (0 in, 2 out)
< 1 BlackHole 2ch, Core Audio (2 in, 2 out)
> 2 External Microphone, Core Audio (1 in, 0 out)
  3 External Headphones, Core Audio (0 in, 2 out)
  4 Mac mini Speakers, Core Audio (0 in, 2 out)

====================

Select an input device:
```

Trong ví dụ này, bạn có thể chọn thiết bị đầu vào 2 (Microphone Bên Ngoài) và thiết bị đầu ra 0 (loa trên màn hình ngoài). Sau khi bạn đã chọn, trở lại máy tính của bạn và làm bất kỳ điều gì bạn muốn, có thể là trình diễn slide hoặc thưởng thức buổi hát karaoke. Âm thanh từ micro sẽ được trộn và phát qua thiết bị đầu ra bạn đã chọn.

## 5. Thông báo từ chối trách nhiệm

Một số điểm quan trọng cần lưu ý:

- Bạn sử dụng Script này tự chịu rủi ro. Người phát triển không chịu trách nhiệm đối với bất kỳ thiệt hại hoặc tác động xấu nào gây ra bởi việc sử dụng Script này.

- Script này đơn giản và có thể có lỗi.

## 6. Gỡ lỗi trên MacOSX

Hãy lưu ý rằng hệ thống bảo mật của MacOSX có thể hạn chế quyền truy cập của Script vào các thiết bị âm thanh. Nếu bạn gặp bất kỳ vấn đề nào, thực hiện các bước sau để cấp quyền cần thiết:

1. Mở Cài đặt Hệ thống.

2. Chuyển đến **Bảo mật và Quyền Riêng Tư**.

3. Chọn **Microphone** từ menu bên trái.

4. Tìm **Terminal** trong danh sách các ứng dụng và đảm bảo rằng nó đã được bật. Điều này cấp quyền cho Script truy cập vào micro của bạn.

Với các cài đặt này đã điều chỉnh, Script của bạn sẽ hoạt động như dự kiến mà không gặp trục trặc nào.

## 7. Người đóng góp

README này và Script được tạo ra với sự hỗ trợ của ChatGPT3.5 (phiên bản miễn phí). Kudos cho sự thần kỳ của trí tuệ nhân tạo!
