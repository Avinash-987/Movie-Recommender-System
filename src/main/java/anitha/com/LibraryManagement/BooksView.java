package anitha.com.LibraryManagement;

public class BooksView {

	public void print(int bid,String bname,String btype)
	{
		System.out.println("BOOK DETAILS:");
		System.out.println("BOOK ID:"+bid);
		System.out.println("BOOK NAME:"+bname);
		System.out.println("AUTHOR:"+btype);
	}
}