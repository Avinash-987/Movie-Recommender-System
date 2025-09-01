package anitha.com.LibraryManagement;

public class BookController {
    private Books model;
    private BooksView view;

    public BookController(Books model, BooksView view) {
        this.model = model;
        this.view = view;
    }

    public void setBookId(int id) {
        model.setBid(id);
    }

    public int getBookId() {
        return model.getBid();
    }

    public void setBookName(String name) {
        model.setBname(name);
    }

    public String getBookName() {
        return model.getBname();
    }

    public void setBtype(String author) {
        model.setBtype(author);
    }

    public String getBtype() {
        return model.getBtype();
    }

    public void updateView() {
        view.print(model.getBid(), model.getBname(), model.getBtype());
    }
}