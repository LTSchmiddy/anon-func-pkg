#
# def teval(
#     p_eval: (str, bool, CodeType, FunctionType),
#     on_true: (str, CodeType, FunctionType, None) = None,
#     on_false: (str, CodeType, FunctionType, None) = None,
#     use_globals: (dict, None) = None,
#     use_locals: (dict, None) = None,
#     p_eval_fargs: tuple = (),
#     on_true_fargs: tuple = (),
#     on_false_fargs: tuple = (),
#     p_eval_fkwargs: (dict, None) = None,
#     on_true_fkwargs: (dict, None) = None,
#     on_false_fkwargs: (dict, None) = None,
#     prefix: str = "anon_func.rexec",
#     dedent: bool = True,
# ) -> Any:
#     """
#     UNTESTED!!
#     :param p_eval:
#     :param on_true:
#     :param on_false:
#     :param use_globals:
#     :param use_locals:
#     :param p_eval_fargs:
#     :param on_true_fargs:
#     :param on_false_fargs:
#     :param p_eval_fkwargs:
#     :param on_true_fkwargs:
#     :param on_false_fkwargs:
#     :param prefix:
#     :param dedent:
#     :return:
#     """
#
#     # Gets the frame for the function call.
#     # Since this code is inside a function, `frames` will always have at least 2 members.
#
#     frame_info = inspect.stack()[1]
#
#     if use_globals is None:
#         use_globals = frame_info.frame.f_globals
#     if use_locals is None:
#         use_locals = frame_info.frame.f_locals
#
#     result = None
#     if isinstance(p_eval, bool):
#         result = p_eval
#     elif isinstance(p_eval, CodeType):
#         result = eval(p_eval, use_globals, use_locals)
#     # Did we get a source code string?
#     elif isinstance(p_eval, str) and p_eval.strip() != "":
#         if dedent:
#             p_eval = textwrap.dedent(p_eval)
#
#         result = eval(
#             compile(p_eval, _get_exec_name(frame_info, prefix), "eval"),
#             use_globals,
#             use_locals,
#         )
#     elif isinstance(p_eval, FunctionType):
#         if p_eval_fkwargs is None:
#             p_eval_fkwargs = {}
#         result = p_eval(*p_eval_fargs, **p_eval_fkwargs)
#     else:
#         result = bool(p_eval)
#
#
#     # Determine which result var to use:
#     r_action, r_fargs, r_fkwargs = tget(result, (on_true, on_true_fargs, on_true_fkwargs), (on_false, on_false_fargs, on_false_fkwargs))
#
#     retVal = None
#     if isinstance(r_action, CodeType):
#         retVal = eval(r_action, use_globals, use_locals)
#     # Did we get a source code string?
#     elif isinstance(r_action, str) and r_action.strip() != "":
#         if dedent:
#             r_action = textwrap.dedent(r_action)
#
#         retVal = eval(
#             compile(r_action, _get_exec_name(frame_info, prefix), "eval"),
#             use_globals,
#             use_locals,
#         )
#     elif isinstance(p_eval, FunctionType):
#         if r_fkwargs is None:
#             r_fkwargs = {}
#         retVal = r_action(*r_fargs, **r_fkwargs)
#
#     else:
#         return r_action
#
#     return retVal
#
#
# def lexec(
#     p_code: (str, CodeType, None) = None,
#     p_return: (str, CodeType, None) = None,
#     prefix: str = "anon_func.rexec",
#     dedent: bool = True
# ) -> Any:
#     frame_info_inner = inspect.stack()[1]
#     frame_info_outer = inspect.stack()[2]
#
#     if frame_info_inner.function != '<lambda>':
#         print("WARNING: `lexec` should only be used inside a lambda function!")
#
#     # print(frame_info_inner.frame.f_globals == frame_info_outer.frame.f_globals)
#
#     use_locals = {}
#     use_locals.update(frame_info_outer.frame.f_locals)
#     use_locals.update(frame_info_inner.frame.f_locals)
#
#     result = rexec(p_code, p_return, frame_info_outer.frame.f_globals, use_locals, prefix, dedent)
#
#     return result