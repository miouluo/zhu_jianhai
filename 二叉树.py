#pragma once
#include <iostream>
using namespace std;
typedef char DataType;

typedef struct Node
{
	DataType data;
	int      Ltag;
	int      Rtag;
	struct Node* LChild;   /*填空1、指针域的数据类型*/
	struct Node* RChild;
}BTNode;

BTNode* pre;
void CreateBiTree(BTNode*& root, DataType Array[]); //创建初始化二叉树
void  Inthread(BTNode* root); //实现中序线索二叉树
BTNode* InPre(BTNode* p);  //求中序线索二叉树结点的前驱
BTNode* InNext(BTNode* p); //求中序线索二叉树结点的后驱

#include "thread.h"          /*2、填空：请填空：包含头文件*/
typedef char DataType;

void CreateBiTree(BTNode*& root, DataType Array[])
{
	static int count = 0;	//静态变量count
	char item = Array[count];//读取Array[]数组中的第count个元素
	count++;
	if (item == '#') //如果读入#字符，创建空树
	{
		root = NULL; return;
	}
	else
	{
		root = (BTNode*)malloc(sizeof(BTNode));/*填空3：生成一个新结点*/
		root->data = item; /*填空4：将ch做为新结点的数据域的值*/
		root->Ltag = 0;
		root->Rtag = 0;
		CreateBiTree(root->LChild, Array); /*填空5: 递归的方法，生成左子树，注意实参的表示方法*/
		CreateBiTree(root->RChild, Array); /*填空6: 递归的方法，生成右子树，注意实参的表示方法*/

	}
}

void  Inthread(BTNode* root)
/* 对root所指的二叉树进行中序线索化，其中pre始终指向刚访问过的结点，其初值为NULL */
{
	if (root != NULL)
	{
		Inthread(root->LChild);  /* 线索化左子树 */
		if (root->LChild == NULL)
		{
			root->Ltag = 1;
			root->LChild = pre;  /*填空7-8：置前驱线索 */
		}
		if (pre != NULL && pre->RChild == NULL)  /* 填空9-10：置后继线索 */
		{
			pre->RChild = root;
			pre->Rtag = 1;
		}
		pre = root;
		Inthread(root->RChild);  /*线索化右子树*/
	}
}

/* 在中序线索二叉树中查找p的中序前驱, 并用pre指针返回结果 */
BTNode* InPre(BTNode* p)
{
	BTNode* q;
	if (p->Ltag == 1)
		q = p->LChild;  /*填空11：直接利用线索找前驱*/
	else
	{ /* 填空12-13：在p的左子树中查找"最右下端"结点 */
		for (q = p->LChild; q->Rtag == 0; q = q->RChild);
		pre = q;
	}
	return(pre);
}

/*在中序线索二叉树中查找p的中序后继结点，并用next指针返回结果*/
BTNode* InNext(BTNode* p)
{
	BTNode* Next;
	BTNode* q;
	if (p->Rtag == 1)
		Next =  p->RChild;  /*填空14：直接利用线索*/
	else
	{ /*填空15-16： 在p的右子树中查找"最左下端"结点*/
		for (q = p->RChild; q->Ltag == 0; q = q->LChild);
		Next = q;
	}
	return(Next);
}

void main()
{
	BTNode* root, * q;
	DataType A[] = "AB#CD##E##F#G##";//以"#"补充空分支后的某个遍历序列

	CreateBiTree(root, A);//以前序遍历序列建立二叉树
	pre = NULL;
	Inthread(root);

	q = InPre(root); /*找根结点的前驱，大家试找其它结点的前驱*/
		cout << root->data << "的前驱为" << q->data << endl;
	q = InNext(root); /*找根结点的后驱，大家试找其它结点的后驱*/
	cout << root->data << "的后继为" << q->data << endl;
};