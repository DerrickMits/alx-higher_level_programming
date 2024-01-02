#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *s, *f;
if (list == NULL || list->next == NULL)
return (0);
s = list;
f = list->next;
while (f != NULL && f->next != NULL)
{
if (s == f)
return (1);
s = s->next;
f = f->next->next;
}
return (0);
}
