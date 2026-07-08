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

bool Search(PNODE head,int No)
{
    while(head != NULL)
    {
        if(head->data == No)
        {
            return true;
        }
        head = head->next;
    }
    
    return false;

}

int main()
{
    PNODE head = NULL;
    bool bRet = false;

    InsertLast(&head,111);
    InsertLast(&head,101);
    InsertLast(&head,51);
    InsertLast(&head,21);
    InsertLast(&head,11);
    
    bRet = Search(head,21);

    if(bRet == true)
    {
        printf("Number is present\n");
    }
    else
    {
        printf("number is nor present\n");
    }

    return 0;
}