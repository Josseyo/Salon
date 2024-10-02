import os

# Set Stripe keys as environment variables
os.environ["STRIPE_PUBLIC_KEY"] = (
    "pk_test_51Q28sSP7j0wPuJKQmqSgJ4kgqTyWrlsQi03lZBbhRMAKZcvaTmoCbLDk4cjvI0bS5p8IUxLVlt0BJ7IWqMMOjViP00DbARntlQ"
)
os.environ["STRIPE_SECRET_KEY"] = (
    "sk_test_51Q28sSP7j0wPuJKQd9By9PTgKGSUFRRk9Q2dUiiyQdJKG4u8oa80jP2cXQj0t14VPVTelAFVzzTmeEYXcjVxL8Kv00TuzQdu4j"
)
os.environ["STRIPE_WH_SECRET"] = "whsec_cdZiCH4tBRukW5PSNJ3Q3ZFnKC4gPyiE"

os.environ["DJANGO_SECRET_KEY"] = (
    "@!7pr8ywn8wgtsolp9^w8dvigjtl*u^hbq23gm6gug1_icdo-m"
)

os.environ.setdefault(
    "DATABASE_URL",
    "postgres://uekmpb0lnen:4aJ7pV0WELJC@ep-gentle-mountain-a23bxz6h-pooler.eu-central-1.aws.neon.tech/stove_five_buggy_670604",
)
