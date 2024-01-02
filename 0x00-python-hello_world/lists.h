#ifndef LISTS_H
#define LISTS_H

typdef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;
size_t print listint(cost listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif
