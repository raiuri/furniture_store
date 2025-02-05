# Order Line
  # order reference
  # Sku
  # quantity

# Batches of stock
  # reference
  # sku
  # quantity

# The name of our unity test describes the behavior that we wanto to see from the sysyem
# and the names of the classes and variables that we use are taken from the business jargon.

from .batch import OrderLine, Batch

def make_batch_and_line(sku, batch_qty, line_qty):
  return (
    Batch(ref=333, sku=sku, quantity=batch_qty),
    OrderLine(sku=sku, order_id='123', quantity=line_qty)
  )


def test_allocating_to_a_batch_reduces_the_available_quantity():
  batch, order_line = make_batch_and_line(sku='BLACK_CHAIR', batch_qty=20, line_qty=3)

  batch.allocate(order_line)

  assert batch.avaliable_qty == 17


def test_can_allocate_if_available_greater_than_required():
  batch, order_line = make_batch_and_line(sku='BLACK_CHAIR', batch_qty=10, line_qty=5)

  assert batch.can_allocate(order_line)


def test_cannot_allocate_if_available_smaller_than_required():
  batch, order_line = make_batch_and_line(sku='BLACK_CHAIR', batch_qty=5, line_qty=10)

  assert batch.can_allocate(order_line) == False


def test_can_allocate_if_available_equal_to_required():
  batch, order_line = make_batch_and_line(sku='BLACK_CHAIR', batch_qty=10, line_qty=10)

  assert batch.can_allocate(order_line)


def test_can_allocate_if_avaliable_greater_than_required():
  pass