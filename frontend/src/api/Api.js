class Api {
  static async login(name) {
    let url = `http://${process.env.VUE_APP_SERVER_DOMAIN}:${process.env.VUE_APP_SERVER_PORT}/login/${name}.json`
    try {
      let res = await fetch(url, {
        method: 'GET',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + process.env.VUE_APP_TOKEN,
        }
      })
      if (res.ok) {
        return await res.json()
      } else {
        return res.status;
      }
    } catch (e) {
      console.log(`Error! ${e}`)
    }
    return false;
  }
}

export default Api