from dataclasses import dataclass
from typing import Optional, Set
from datetime import date

# Order Line
  # order reference
  # sku
  # quantity

# Batches of stock
  # reference
  # sku
  # quantity

@dataclass(frozen=True)
class OrderLine:
  order_id: str
  sku: str
  quantity: int


class Batch:
  batches = set()

  def __init__(self, ref: str, sku: str, quantity: int):
    self.ref = ref
    self.sku = sku
    self._purchased_quantity = quantity
    self._allocations = set() # type: Set[OrderLine]


  def can_allocate(self, order_line: OrderLine) -> bool:
    return self.available_quantity >= order_line.quantity and self.sku == order_line.sku


  def allocate(self, order_line: OrderLine) -> int:
    if self.can_allocate(order_line):
      self._allocations.add(order_line)


  def deallocate(self, order_line: OrderLine):
    if order_line in self._allocations:
      self._allocations.remove(order_line)
  

  @property
  def allocated_qunatity(self) -> int:
    return sum(order_line.quantity for order_line in self._allocations)
  
  @property
  def available_quantity(self):
    return self._purchased_quantity - self.allocated_qunatity
  