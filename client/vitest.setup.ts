import { library } from "@fortawesome/fontawesome-svg-core"
import { faTrash } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome"
import { config } from "@vue/test-utils"

library.add(faTrash)
config.global.components = {
    "font-awesome-icon": FontAwesomeIcon
}
