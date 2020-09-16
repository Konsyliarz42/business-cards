from faker import Faker
from businessCard import BusinessCard

def generate_business_card(quantity=1):
    business_cards = list()
    fake = Faker('pl_PL')

    for _ in range(quantity):
        bcard = BusinessCard(   fake.first_name(),
                                fake.last_name(),
                                fake.company(),
                                fake.job(),
                                fake.email(),
                                fake.phone_number()    )

        business_cards.append(bcard)

    return business_cards

if __name__ == "__main__":
    cards = generate_business_card(5)

    by_first_name   = sorted(cards, key=lambda card: card.first_name)
    by_last_name    = sorted(cards, key=lambda card: card.last_name)
    by_email        = sorted(cards, key=lambda card: card.email)

    for card in by_first_name:
        print(card)
    print('')

    for card in by_last_name:
        print(card)
    print('')

    for card in by_email:
        print(card)
    print('')

    for card in cards:
        card.contact()
    print('')

    for card in cards:
        print(card.length_name)