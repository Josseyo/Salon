import os

# Set Stripe keys as environment variables
os.environ["STRIPE_PUBLIC_KEY"] = (
    "pk_test_51Q28sSP7j0wPuJKQmqSgJ4kgqTyWrlsQi03lZBbhRMAKZcvaTmoCbLDk4cjvI0bS5p8IUxLVlt0BJ7IWqMMOjViP00DbARntlQ"
)
os.environ["STRIPE_SECRET_KEY"] = (
    "sk_test_51Q28sSP7j0wPuJKQd9By9PTgKGSUFRRk9Q2dUiiyQdJKG4u8oa80jP2cXQj0t14VPVTelAFVzzTmeEYXcjVxL8Kv00TuzQdu4j"
)
os.environ["STRIPE_WH_SECRET"] = "whsec_cdZiCH4tBRukW5PSNJ3Q3ZFnKC4gPyiE"