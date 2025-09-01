package anitha.com.LibraryManagement;

public class Books {
	int bid;
	String bname;
	String btype;
	public Books(int bid,String bname,String btype) {
		this.bid=bid;
		this.bname=bname;
		this.btype=btype;
	}
	public int getBid() {
		return bid;
	}
	public void setBid(int bid) {
		this.bid = bid;
	}
	public String getBname() {
		return bname;
	}
	public void setBname(String bname) {
		this.bname = bname;
	}
	public String getBtype() {
		return btype;
	}
	public void setBtype(String btype) {
		this.btype = btype;
	}
	
}
