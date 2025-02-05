from dataclasses import dataclass
from typing import Optional
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
    self.avaliable_qty = quantity
    self._allocations = set()


  def can_allocate(self, order_line: OrderLine) -> bool:
    if self.avaliable_qty < order_line.quantity:
      return False
    if self.sku != order_line.sku:
      return False
    return True


  def allocate(self, order_line: OrderLine) -> int:
    self.can_allocate(order_line)
    self._allocations.add(order_line)
    self.avaliable_qty -= order_line.quantity


order_line = OrderLine(sku='BLACK_CHAIR', order_id='123', quantity=5)
batch = Batch(ref=333, sku='BLACK_CHAIR', quantity=10)
  
print(batch.can_allocate(order_line))
