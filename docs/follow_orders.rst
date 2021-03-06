**********************
Follow Orders Strategy
**********************

This strategy places a buy and a sell walls into a specific market.
It buys below a base price, and sells aboe the base price.

It then reacts to orders filled (hence the name), when one order is
completely filled, new walls are constructed using the filled order
as the new base price.

Configuration Questions
=======================

Spread
------

Percentage difference between buy and sell price. So a spread of 5% means the bot sells at 2.5%
above the base price and buys 2.5% below.

Wall
----

This is the "wall height": the default amount to buy/sell, in quote. So if you are on the AUD:BTS
market, this is the amount to buy/sell in AUD.

Max
---

The bot will stop trading if the base price goes above this value, it will shut down until you manually
restart it. (i.e. it won't restart itself if the price drops)

Remember prices are base/quote, so on AUD:BTS, that's the price of 1 AUD in BTS.

Min
---

Same in reverse: stop running if prices go below this value.

Start
-----

The initial base price, as a percentage of the settlement price. So "103" here means an initial base price 3%
above the settlement price. (Yes I know not all BTS markets have a settlement price, currently the bot won't
work in those)

Reset
-----

Normally the bot checks if it has previously placed orders in the market and uses those. If true,
this option forces the bot to cancel any existing orders when it starts up, and calculate
the starting price from the settlement price as above.

Staggers
--------

Number of additional (or "staggered") orders to place. By default this is "1" (so
no additional orders). The gap between each order is the same as between the first orders
and the base price (that is, half the spread).

So say the spread is 5% and staggers is "2", then there will be 2
buy orders: 2.5% and 5% below the base price, and two sells 2.5% and 5% above.
The order amounts are all the same (see `wall` option)


Bot problems
============

Like all liquidity bots, the bot really works best with a "even"
market, i.e. where are are counterparties both buying and selling.

With a severe "bear" market, the
bot can be stuck being the sole participant that is still buying against panicked humans frantically selling.
It repeatingly buys into the market and so it can
run out of one asset quite quickly (although it will have bought it at
lower and lower prices).

I don't have a simple good solution (and happy to hear suggestions from experienced traders)

I plan a smarter bot that will change its behaviour when it starts to runs low on an asset,
but this will have a different name.
