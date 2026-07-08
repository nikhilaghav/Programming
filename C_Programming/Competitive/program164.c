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

int Frequency(PNODE head, int No)
{
    int iCount = 0;

     while(head != NULL)
    {
        if((head->data) == No )
        {
            iCount++;
        }
        head = head->next;
    }

    return iCount;
}

int main()
{
    PNODE head = NULL;
    int iRet = 0;

    InsertLast(&head,111);
    InsertLast(&head,21);
    InsertLast(&head,21);
    InsertLast(&head,21);
    InsertLast(&head,10);
    
    iRet = Frequency(head,21);
    printf("frequency is: %d\n",iRet);

    return 0;
}