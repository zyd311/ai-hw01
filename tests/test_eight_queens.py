# 八皇后求解器的单元测试
import pytest
from src.eight_queens import solve_n_queens

def test_n_queens_4():
    """测试4皇后：正确解数量是2"""
    assert len(solve_n_queens(4)) == 2

def test_n_queens_8():
    """测试8皇后：正确解数量是92"""
    assert len(solve_n_queens(8)) == 92

def test_n_queens_edge_cases():
    """测试边界情况"""
    assert len(solve_n_queens(1)) == 1  # 1皇后：1个解
    assert len(solve_n_queens(2)) == 0  # 2皇后：无解
    assert len(solve_n_queens(3)) == 0  # 3皇后：无解