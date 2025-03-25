#
good_input = 'Google'
malicious_input = "'; drop table customers; -- "  # input would come from a web form, for instance

naive_format = "select * from customers where company_name = '{}' and company_id != 0"

good_query = naive_format.format(good_input)  # string formatting naively adds the user input to a field, expecting only a customer name
malicious_query = naive_format.format(malicious_input)  # string formatting naively adds the user input to a field, expecting only a customer name

print("Good query:")
print(good_query)  # non-malicious input works fine
print()

print("Bad query:")
print(malicious_query)  # query now drops a table ('--' is SQL comment)
