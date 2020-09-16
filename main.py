import random
from faker import Faker
from businessCard import BusinessCard, BaseContact, BusinessContact

#----------------------------------------------------------------
def generate_business_card(quantity=1):
    business_cards = list()
    fake = Faker('pl_PL')

    for _ in range(quantity):
        bcard = BusinessCard(   fake.first_name(),
                                fake.last_name(),
                                fake.phone_number() )

        business_cards.append(bcard)

    return business_cards

#----------------------------------------------------------------
def create_contacts(quantity=1):
    bcards  = list()
    fake = Faker('pl_PL')

    for _ in range(quantity):
        if random.randrange(2) == 0:
            bcard = BaseContact(    fake.email(),
                                    fake.first_name(),
                                    fake.last_name(),
                                    fake.phone_number() )
        else:
            bcard = BusinessContact(    fake.company(),
                                        fake.job(),
                                        fake.first_name(),
                                        fake.last_name(),
                                        fake.phone_number() )
                                        
        bcards.append(bcard)

    return bcards
    
#================================================================
if __name__ == "__main__":
    first_name      = 'Natan'
    last_name       = 'Bodych'
    email           = 'natan78@gmail.com'
    phone_number    = '+48 32 032 71 77'
    work_number     = '664 680 015'
    company         = 'Bojczuk s.c.'
    job             = 'Hutnik'

    base_contact        = BaseContact(email, first_name, last_name, phone_number)
    business_contact    = BusinessContact(company, job, first_name, last_name, work_number)

    base_contact.contact()
    business_contact.contact()

    print(base_contact.label_length)

    print(create_contacts(3))