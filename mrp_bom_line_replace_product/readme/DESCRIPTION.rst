This module allows you to specify a replacement product and quantity on a BoM line,
if the BoM type is 'kit' (phantom). When the kit is produced in conjunction with
other products as part of the same batch, the batch will be searched for the
replacement product, of which the specified quantity will be removed (its move
will be cancelled).

This enables to use certain products as so-called 'upgrade products'. For example
if the main kit contains a machine type 1000, but people pay a slight bit more to
have the machine type 1001, the 'upgrade product' could also be a kit that contains
the 1001, but with replacement product 1000: if the 1000 is also in the picking,
it will be removed.
