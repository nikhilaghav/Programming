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

int FirstOccur(PNODE head, int No)
{
    int iCount = 1;

    while(head != NULL)
    {
        if((head->data) == No )
        {
            return iCount;
        }
        iCount++;
        head = head->next;
    }
    return -1;

    printf("\n");
}

int main()
{
    PNODE head = NULL;
    int iRet = 0;

    InsertLast(&head,10);
    InsertLast(&head,20);
    InsertLast(&head,30);
    InsertLast(&head,20);
    InsertLast(&head,50);

    iRet = FirstOccur(head,20);
    if(iRet ==-1)
    {
        printf("Number is not present\n");
    }
    else
    {
        printf("first occcurence is at:%d\n",iRet);
    }
    return 0;
}