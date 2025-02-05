# Order Line
  # order reference
  # Sku
  # quantity

# Batches of stock
  # reference
  # sku
  # quantity

from .batch import OrderLine, Batch

def test_allocating_to_a_batch_reduces_the_available_quantity():
  order_line = OrderLine(sku='BLACK_CHAIR', order_id='123', quantity=3)
  batch = Batch(ref=333, sku='BLACK_CHAIR', quantity=20)

  batch.allocate(order_line)

  assert batch.avaliable_qty == 17


def test_can_allocate_if_available_greater_than_required():
  order_line = OrderLine(sku='BLACK_CHAIR', order_id='123', quantity=5)
  batch = Batch(ref=333, sku='BLACK_CHAIR', quantity=10)

  assert batch.can_allocate(order_line)


def test_cannot_allocate_if_available_smaller_than_required():
  order_line = OrderLine(sku='BLACK_CHAIR', order_id='123', quantity=10)
  batch = Batch(ref=333, sku='BLACK_CHAIR', quantity=5)

  assert batch.can_allocate(order_line) == False


def test_can_allocate_if_available_equal_to_required():
  order_line = OrderLine(sku='BLACK_CHAIR', order_id='123', quantity=5)
  batch = Batch(ref=333, sku='BLACK_CHAIR', quantity=5)

  assert batch.can_allocate(order_line)