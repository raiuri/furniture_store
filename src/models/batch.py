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
  def __init__(self, ref: str, sku: str, quantity: int):
    self.ref = ref
    self.sku = sku
    self.avaliable_qty = quantity


  def allocate(self, order_line: OrderLine):
    self.avaliable_qty -= order_line.quantity

