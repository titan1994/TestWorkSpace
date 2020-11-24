def new_ext_file_path(file_input_path, new_suf):
    """
    Возвращает путь к файлу по файлу. ...learn.txt->...learn.<new_suf>
    :param file_input_path:
    :param new_suf:
    :return:
    """
    file_new = str(file_input_path.name).replace(file_input_path.suffix, new_suf)
    new_path = file_input_path.parent.joinpath(file_input_path.parent, file_new)
    return new_path

