class Api {
  static async login(name) {
    let url = `http://${process.env.VUE_APP_SERVER_DOMAIN}:${process.env.VUE_APP_SERVER_PORT}/login/${name}.json`
    let res = await fetch(url, {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Authorization': 'Bearer ' + process.env.VUE_APP_TOKEN,
      }
    })
    if (res.ok) {
      return await res.json()
    } else {
      return false;
    }
  }
}

export default Api