import datetime;

class Company:
    def __init__(self, n, m):
        self.n = n;
        self.m = m;
    def getFloors(self):
        return self.n;
    def getElevators(self):
        return self.m;
    
        
        
class History:
    def __init__(self, floor, elevator, time):
        self.floor = floor;
        self.elevator = elevator;
        self.time = time;
    def getHistory(self):
        return self.floor, self.elevator, self.time;
    
allHistory = [];
c = Company(5, 10);

def resolveElevator(n, m, x) : #n: số tần, m: số thang máy, x: tầng hiện tại đang đứng.
    ans = str(input('Would you like to continue using the elevator? (y/n)'));
    if (ans == 'n'):
        return 0;
    else:
        a = int(input('Which elevator do you choose?')); # người khách chọn 1 trong m thang máy mà họ muốn vào. 
        if ((a > m) | (a <= 0)): 
            print('Thang máy này hiện không tồn tại trong hệ thống');
            return resolveElevator(n, m, x);
        b = int(input('Which floor do you want to go to?')); #tầng mà người đó chọn
        if (b > n | b <= 0):
            print('Công ty hiện tại chỉ có: ' + n + 'tầng');
            return resolveElevator(n, m, x);
        elif (b == x): 
            print('Bạn hiện đang ở tầng này');
            return resolveElevator(n, m, x);
        his = History(b, a, datetime.datetime.now());
        allHistory.append(his);
        return resolveElevator(n, m, b);

run = True;
while run:
    n = c.getFloors();
    m = c.getElevators();
    y = resolveElevator(n, m, 0);
    if (y == 0):
        break;

print(len(allHistory));
# Trong thực tế nếu lập trình 1 app thì có thể dùng đồn thời song song nhiều máy tính,
# các client gửi thông tin để lưu lại server nhưng đây là mô phỏng nên em chỉ có thể viết được như vậy.
# Vì em không biết mối liên hệ giữa biến m và n kiểu như 1 tầng có bao nhiêu thang máy hay gì nên em cho mỗi tầng có M thang máy.
    



        