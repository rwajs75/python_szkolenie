Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname> and <lastname>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname | lastname |
  | Nazwisko1 | Imie1    |
  | Nazwisko2 | Imie2    |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without deleted contact


Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I modify the contact from the list
  Then the modify contact list is equal to the old list without modified contact