import time

class SeatLockSystem:
    def __init__(self):
        self.locked_seats = {}
        self.timeout = 60  # 锁定超时时间：60秒

    def lock(self, seat_id, user):
        """
        尝试锁定座位
        如果座位未锁定，或锁定已过期，则锁定成功。
        """
        now = time.time()
        # 检查是否已被锁定且未过期
        if seat_id in self.locked_seats and self.locked_seats[seat_id]['expire'] > now:
            return False
        
        # 锁定座位 (更新过期时间)
        self.locked_seats[seat_id] = {'user': user, 'expire': now + self.timeout}
        return True

    def is_locked(self, seat_id):
        """
        检查座位当前是否处于锁定状态
        """
        now = time.time()
        if seat_id in self.locked_seats and self.locked_seats[seat_id]['expire'] > now:
            return True
        return False