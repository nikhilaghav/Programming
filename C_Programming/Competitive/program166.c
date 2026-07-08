#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

#pragma pack(1)
struct node
{
    int data;
    struct node* next;
    
};

typedef struct node NODE;
typedef struct node* PNODE;
typedef struct node** PPNODE;


void InsertLast(PPNODE first, int iNo)
{
    PNODE newn = NULL;
    PNODE temp = NULL;

    newn = (PNODE)malloc(sizeof(NODE));

    newn->data = iNo;
    newn->next = NULL;

    if(*first == NULL)
    {
        *first = newn;
    }
    else
    {
        temp = *first;

        while (temp->next != NULL)
        {
            temp = temp->next;
        }
        temp->next = newn;
        
    }
}

void DisplayOdd(PNODE head)
{
    while(head != NULL)
    {
        if((head->data) % 2 != 0 )
        {
            printf("%d ",head->data);
        }
        head = head->next;
    }
    printf("\n");
}

int main()
{
    PNODE head = NULL;

    InsertLast(&head,111);
    InsertLast(&head,101);
    InsertLast(&head,50);
    InsertLast(&head,20);
    InsertLast(&head,10);

    DisplayOdd(head);

    return 0;
}