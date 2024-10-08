#  result.py
#  Created by Kiro Shin <mulgom@gmail.com> on 2023.
#
#  https://doc.rust-lang.org/std/result/enum.Result.html
#  https://developer.apple.com/documentation/swift/result
#  https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-result/
#
#  이런 게 없어도 크게 불편한 건 없고 오히려 언랩핑으로 불편하지만, 요즘 대세에 따라 조금 더 명확하게 하기 위해 굳이 만든다.
#  Result 가 러스트 외 다른 언어에서도 따라서 등장하는 걸 보면 파이썬도 곧 생길 것 같다. 적당히 당장 쓸 것만 작성해둔다.
#

from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic, Callable, final

__all__ = ['Result', 'Ok', 'Err']

T = TypeVar("T", covariant=True)  # 성공타입
E = TypeVar("E", covariant=True)  # 에러타입(도메인 지정)
M = TypeVar("M")
N = TypeVar("N")


# ----------------------------------------
# 추상타입
# ----------------------------------------
class _Result(metaclass=ABCMeta):
    __match_args__ = ("_value",)
    __slots__ = ("_value",)

    # equal to: x == y
    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__) and self._value == other._value

    # not equal to: x != y
    def __ne__(self, other) -> bool:
        return not (self == other)

    # __REPL__ OFFICIAL: Representation for Developer
    # __STR__  INFORMAL: to string for User
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._value})"

    # [ Value ] ----------------------------------------
    @abstractmethod
    def ok(self) -> object | None:
        """Ok -> T | Err -> None"""

    @abstractmethod
    def err(self) -> object | None:
        """Ok -> None | Err -> E"""

    @abstractmethod
    def unwrap_or(self, df) -> object:
        """Ok -> T | Err -> df"""

    @abstractmethod
    def unwrap_or_else(self, op: Callable[..., object]) -> object:
        """Ok -> T | Err -> op(E) -> M"""

    @abstractmethod
    def map_or(self, df, op: Callable[..., object]) -> object:
        """Ok -> op(T) -> M  //  Err -> narmal"""

    @abstractmethod
    def map_or_else(self, df: Callable[..., object], op: Callable[..., object]) -> object:
        """Ok -> op(T) -> M  //  Err -> df(E) -> M"""

    # [ Monad ] ----------------------------------------
    @abstractmethod
    def and_(self, res: '_Result') -> '_Result':
        """Ok1 && Ok2 -> Ok2  //  Ok1 && Err1 -> Err1  //  Err1 && Err2 -> Err1"""

    @abstractmethod
    def and_then(self, op: Callable[..., '_Result']) -> '_Result':
        """Ok -> op(Ok2) -> Result  //  Err -> Err"""

    @abstractmethod
    def or_(self, res: '_Result') -> '_Result':
        """Ok1 || Ok2 -> Ok1  //  Ok1 || Err1 -> Ok1  //  Err1 && Ok1 -> Ok1  //  Err1 && Err2 -> Err2"""

    @abstractmethod
    def or_else(self, op: Callable[..., '_Result']) -> '_Result':
        """Ok -> Ok  //  Err -> op(E) -> Result"""

    @abstractmethod
    def map(self, op: Callable[..., object]) -> '_Result':
        """Ok -> op(T) -> M -> Ok(M)  //  Err -> pass"""


# ----------------------------------------
# 성공타입
# ----------------------------------------
@final
class Ok(Generic[T], _Result):
    def __init__(self, value: T) -> None:
        self._value = value

    def ok(self) -> T:
        return self._value

    def err(self) -> None:
        return None

    def unwrap_or(self, _) -> T:
        return self._value

    def unwrap_or_else(self, _) -> T:
        return self._value

    def and_(self, res: 'Result[M, N]') -> 'Result[M, N]':
        return res

    def and_then(self, op: Callable[[T], 'Result[M, N]']) -> 'Result[M, N]':
        return op(self._value)

    def or_(self, _) -> 'Ok[T]':
        return self

    def or_else(self, _) -> 'Ok[T]':
        return self

    def map(self, op: Callable[[T], M]) -> 'Ok[M]':
        return Ok(op(self._value))

    def map_or(self, _, op: Callable[[T], N]) -> N:
        return op(self._value)

    def map_or_else(self, df: Callable[[E], N], op: Callable[[T], N]) -> N:
        return op(self._value)


# ----------------------------------------
# 실패타입
# ----------------------------------------
@final
class Err(Generic[E], _Result):
    def __init__(self, value: E) -> None:
        self._value = value

    def ok(self) -> None:
        return None

    def err(self) -> E:
        return self._value

    def unwrap_or(self, df: T) -> T:
        return df

    def unwrap_or_else(self, op: Callable[[E], 'Result[M, N]']) -> 'Result[M, N]':
        return op(self._value)

    def and_(self, _) -> 'Err[E]':
        return self

    def and_then(self, _) -> 'Err[E]':
        return self

    def or_(self, res: 'Result[M, N]') -> 'Result[M, N]':
        return res

    def or_else(self, op: Callable[[E], 'Result[M, N]']) -> 'Result[M, N]':
        return op(self._value)

    def map(self, _) -> 'Err[E]':
        return self

    def map_or(self, df: M, _) -> M:
        return df

    def map_or_else(self, df: Callable[[E], N], op: Callable[[T], N]) -> N:
        return df(self._value)


# ----------------------------------------
# 유니온 타입 지정 - 파이썬에서는 이게 최선이다.
#   굳이 통합해서 구현하게 되면 내부에 타입변수 하나 더 소비하게 되고, 매칭 탐색으로 처리해야 한다.
# ----------------------------------------
Result = Ok[T] | Err[E]

