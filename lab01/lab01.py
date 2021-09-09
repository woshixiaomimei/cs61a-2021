def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k>0:
        fall_mul=1
        while k>0:
            fall_mul, n, k = fall_mul*n, n-1, k-1
        return fall_mul
    else:
        return 1


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    cnt, fig_num=y//10, 1  #fig_num: number of figures
    while cnt>=1:
        cnt, fig_num=y//(10**(fig_num+1)), fig_num+1
    cnt_sum=0
    while fig_num>=1:
        cnt_sum, y, fig_num=cnt_sum+y//(10**(fig_num-1)), y%(10**(fig_num-1)), fig_num-1    
    return cnt_sum


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    cnt, fig_num=n//10, 1  #fig_num: number of figures
    while cnt>=1:
        cnt, fig_num=n//(10**(fig_num+1)), fig_num+1    
    flag=1
    while fig_num>=1 and flag==1:
        if n//(10**(fig_num-1))==8 and (n%(10**(fig_num-1)))//(10**(fig_num-2))==8:
            cnt_88, flag=1, 0
        else:
            n=n%(10**(fig_num-1))
            cnt_88, flag, fig_num=0, 1, fig_num-1
    return cnt_88==1
            
