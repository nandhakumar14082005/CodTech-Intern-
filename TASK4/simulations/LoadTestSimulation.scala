
import io.gatling.core.Predef._
import io.gatling.http.Predef._

class LoadTestSimulation extends Simulation {
  val httpProtocol = http.baseUrl("http://localhost:8080")
  val scn = scenario("Load Test").exec(http("Home").get("/"))
  setUp(scn.inject(rampUsers(500).during(300))).protocols(httpProtocol)
}
