#define LISTS_H
#ifndef LISTS_H
#include <stdlib.h>
/**
 * struct listint_s - singly linked list
 * @num: value of integer
 * @next: function  to the next node
 *
 * Description: function singly linked list node structure
 * for project
 */
typedef struct listint_s
{
int num;
struct listint_s *next;
} listint_t;
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);
#endif 
