#!/usr/bin/env python

"""Prepare SQL statements to fill contact relationships
- start_msisdn: msisdn to start with
- no_of_contacts: how many contacts a user will have
- no_of_users: how many users will be prepared
"""

import sys

def write_to_file(result_queries, filename):
    with open(filename, "w") as f:
        for query in result_queries:
            f.write(query)
            f.write("\n")

def create_contact_rels(start_user, no_contacts, user_contacts):
    """Prepare contacts with a modulo-based algorithm:
    u1: u2, u3, u4
    u2: u3, u4, u1
    u3: u4, u2, u1
    u4: u1, u2, u3
    """

    for user in range(start_user, start_user + no_contacts):
#        print "Create Contacts for user: {0} no_contacts {1}".format(user, no_contacts)
        contacts = list()
        for idx in range(start_user, user):
            contacts.append(idx)
        for idx in range(1, no_contacts - len(contacts) ):
            contacts.append(user + idx)
#        print contacts
        assert(len(contacts) == no_contacts-1)
        user_contacts[user] = contacts

def prepare_sql_statements(start_msisdn, number_contacts, number_users, filename):
    """Prepare ContactRelationships for number_users"""

    user_contacts = dict()
    BATCH_SIZE=number_users/number_contacts
    tmp = 0
    for idx in range(0, BATCH_SIZE):
        create_contact_rels(start_msisdn + idx * number_contacts, number_contacts, user_contacts)
        tmp += 1

    remaining = number_users % number_contacts
    if remaining != 0:
        create_contact_rels(start_msisdn + (idx +1) * number_contacts, remaining, user_contacts)

#    print "user_contacts size {0}".format(user_contacts)
    assert(len(user_contacts) == number_users)

    result_queries = list()

    INSERT_QUERY = "INSERT INTO `ContactRelationship` (`ksOwnerEndUser`, `ksTargetEndUser`, `eStatus`, `sDisplayName`) VALUES "
    for user, contacts in user_contacts.iteritems():
        current_query = INSERT_QUERY
        for current_contact in contacts:
            current_query += "('+{0}','+{1}','{2}','+{3}'),".format(user, current_contact, 1, current_contact)
        result_queries.append(current_query[:-1] + ";")

    write_to_file(result_queries, filename)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print "usage: ./insert_relations.py <start_msisdn> <no_of_contacts> <no_of_users> <output_file>"
        sys.exit(1)
    start_msisdn = int(sys.argv[1])

    START_USER = 4100000
    END_USER = 4109999
    if start_msisdn < START_USER or start_msisdn > END_USER:
        print "start_msisdn must be in [{0}, {1}]".format(START_USER, END_USER)
        sys.exit(2)

    number_contacts = int(sys.argv[2]) + 1
    if number_contacts <= 0 or number_contacts > (END_USER - START_USER):
        print "no_of_contacts must be in (0, {0})".format(END_USER - START_USER)
        sys.exit(3)

    number_users = int(sys.argv[3])
    if number_users <= 0 or number_users > (END_USER - START_USER):
        print "no_of_users must be in (0, {0})".format(END_USER - START_USER)
        sys.exit(4)

    output_file = sys.argv[4]

    prepare_sql_statements(start_msisdn, number_contacts, number_users, output_file)
