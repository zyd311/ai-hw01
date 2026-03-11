# 八皇后问题求解器 - 回溯法实现
def solve_n_queens(n):
    """
    求解N皇后问题的所有合法方案
    :param n: 棋盘大小（皇后数量）
    :return: 所有解的列表，每个解是一维数组（索引=行，值=列）
    """
    solutions = []  # 存储所有合法解
    
    def backtrack(row, cols, diags1, diags2, path):
        # 递归终止条件：所有行都放好皇后
        if row == n:
            solutions.append(path.copy())
            return
        
        # 遍历当前行的每一列，尝试放皇后
        for col in range(n):
            # 计算当前位置的两个对角线标识
            d1 = row - col  # 左上-右下对角线
            d2 = row + col  # 右上-左下对角线
            
            # 检查列、对角线是否已有皇后（无冲突才放）
            if col not in cols and d1 not in diags1 and d2 not in diags2:
                # 放置皇后（记录占用的列和对角线）
                cols.add(col)
                diags1.add(d1)
                diags2.add(d2)
                path.append(col)
                
                # 递归处理下一行
                backtrack(row + 1, cols, diags1, diags2, path)
                
                # 回溯：撤销当前皇后的放置
                path.pop()
                diags2.remove(d2)
                diags1.remove(d1)
                cols.remove(col)
    
    # 从第0行开始回溯，初始无皇后
    backtrack(0, set(), set(), set(), [])
    return solutions

# 测试示例（运行代码时可查看结果）
if __name__ == "__main__":
    # 输出8皇后的解的数量（应该是92）
    print(f"8皇后问题的解数量：{len(solve_n_queens(8))}")