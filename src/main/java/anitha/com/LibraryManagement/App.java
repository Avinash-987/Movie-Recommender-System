package anitha.com.LibraryManagement;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
    	 Books book = new Books(1, "The Alchemist", "Paulo Coelho");
         BooksView view = new BooksView();
         BookController controller = new BookController(book, view);
         controller.updateView();
    }
}
