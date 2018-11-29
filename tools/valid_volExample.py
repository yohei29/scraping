from voluptuous import Schema, Match

schema = Schema({
    'name':str,
    'price':Match(r'^[0-9,]+$'),
}, required=True)

schema({
    'name':'grape',
    'price':500,
})

schema({
    'name':'grape',
    'price':'500',
})