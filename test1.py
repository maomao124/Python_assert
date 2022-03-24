"""
 * Project name(项目名称)：Python_assert断言
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/24 
 * Time(创建时间)： 20:28
 * Version(版本): 1.0
 * Description(描述)： assert 语句，又称断言语句，可以看做是功能缩小版的 if 语句，它用于判断某个表达式的值，
 如果值为真，则程序可以继续往下执行；反之，Python 解释器会报 AssertionError 错误。
 """

if __name__ == '__main__':
    mathmark = int(input())
    # 断言数学考试分数是否位于正常范围内
    assert 0 <= mathmark <= 100
    # 只有当 mathmark 位于 [0,100]范围内，程序才会继续执行
    print("数学考试分数为：", mathmark)
