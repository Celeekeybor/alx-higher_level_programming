#include "lists.h"

/**
 * check_cycle -  checks if a singly linked list has a cycle in it
 * @list: pointer to the node
 * Return: true or false
 */
int check_cycle(listint_t *list)
{
listint_t *current, *check;
if (list == NULL || list->next == NULL)
return (0);
current = list;
check = current->next;
while (current != NULL && check->next != NULL
&& check->next->next != NULL)
{
if (current == check)
return (1);
current = current->next;
check = check->next->next;
}
return (0);
}
