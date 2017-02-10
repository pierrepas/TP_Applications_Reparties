package example;
import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.xml.ws.Endpoint;

/**
 * Created by drey on 03/02/17.
 */
@WebService()
public class CalcDistance {
  @WebMethod
  public double calcKm(double latVille1, double longVille1, double latVille2, double longVille2) {
    double result = calculerKm(latVille1,longVille1,latVille2,longVille2);
    System.out.println("Distance : "+result);
    return result;
  }

  private double calculerKm(double latVille1, double longVille1, double latVille2, double longVille2) {
    double delta = longVille2-longVille1;
    double Sab=Math.acos(Math.sin(latVille1)*Math.sin(latVille2)+Math.cos(latVille1)*Math.cos(latVille2)*delta);
    

    return Sab * 6378137; //rayon de la terre

  }

  public static void main(String[] argv) {
    Object implementor = new CalcDistance ();
    String address = "http://localhost:9000/CalcDistance";
    Endpoint.publish(address, implementor);
  }
}
