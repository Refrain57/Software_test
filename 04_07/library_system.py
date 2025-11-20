class LibrarySystem:
    def __init__(self):
        # 初始化模拟数据
        # 用户列表 (使用集合存储用户名)
        self.users = {"Alice", "Bob", "Charlie"}
        
        # 图书库存 (书名: 库存数量)
        self.books = {
            "Python编程从入门到实践": 5,
            "算法导论": 2,
            "绝版孤本": 1,
            "被借光的书": 0
        }

    def borrow_book(self, user: str, book: str) -> bool:
        """
        借书功能函数
        :param user: 用户名
        :param book: 书名
        :return: 借阅成功返回 True
        :raises: ValueError 如果用户不存在、书不存在或库存为0
        """
        # 1. 检查用户是否存在
        if user not in self.users:
            raise ValueError(f"错误：用户 '{user}' 不存在")

        # 2. 检查图书是否存在
        if book not in self.books:
            raise ValueError(f"错误：图书 '{book}' 未收录")

        # 3. 检查库存是否充足
        if self.books[book] <= 0:
            raise ValueError(f"错误：图书 '{book}' 目前无库存")

        # 4. 借书后库存减少
        self.books[book] -= 1
        print(f"借阅成功：{user} 借走了 《{book}》，剩余库存：{self.books[book]}")
        
        return True

# 用于手动调试的简单的入口 (可选)
if __name__ == "__main__":
    lib = LibrarySystem()
    try:
        lib.borrow_book("Alice", "Python编程从入门到实践")
    except Exception as e:
        print(e)