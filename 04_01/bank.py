def transfer(accountA, accountB, amount):
    """
    在两个账户之间转账。
    
    :param accountA: 转出账户 (字典，包含 'balance' 键)
    :param accountB: 转入账户 (字典，包含 'balance' 键)
    :param amount: 转账金额
    :return: 成功返回 True
    :raises ValueError: 如果金额非正数或余额不足
    """
    if amount <= 0:
        raise ValueError("转账金额必须为正数")
    
    if accountA['balance'] < amount:
        raise ValueError("余额不足")
    
    accountA['balance'] -= amount
    accountB['balance'] += amount
    
    return True