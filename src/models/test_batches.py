# Order Line
  # order reference
  # Sku
  # quantity

# Batches of stock
  # reference
  # sku
  # quantity

from .batch import OrderLine, Batch

def test_allocating_to_a_batch_reduces_the_avaliable_quantity():
  order_line = OrderLine(sku='abc', order_id='123', quantity=3)
  batch = Batch(ref=333, sku='abc', quantity=20)

  batch.allocate(order_line)

  assert batch.avaliable_qty == 17


